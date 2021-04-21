from faker import Faker
from src.data.test import FindUserSpy
from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_user_controller import FindUserController


faker = Faker()


def test_route():
    """ Testing Route method """

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest(
        query={"user_id": faker.random_number(), "user_name": faker.word()}
    )

    response = find_user_controller.route(http_request)

    # Testing Inputs
    assert (
        find_user_use_case.by_id_and_name_param["user_id"]
        == http_request.query["user_id"]
    )
    assert (
        find_user_use_case.by_id_and_name_param["name"]
        == http_request.query["user_name"]
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_route_no_query_param():
    """ Testing Route method """

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest()

    response = find_user_controller.route(http_request)

    # Testing Inputs
    assert find_user_use_case.by_id_and_name_param == {}
    assert find_user_use_case.by_id_param == {}
    assert find_user_use_case.by_name_param == {}

    # Testing Output
    assert response.status_code == 400
    assert "error" in response.body


def test_route_query_params_error():
    """ Testing Route method """

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest(
        query={"id": faker.random_number(), "name": faker.word()}
    )

    response = find_user_controller.route(http_request)

    # Testing Inputs
    assert find_user_use_case.by_id_and_name_param == {}
    assert find_user_use_case.by_id_param == {}
    assert find_user_use_case.by_name_param == {}

    # Testing Output
    assert response.status_code == 422
    assert "error" in response.body
