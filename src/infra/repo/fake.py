from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class FakerRepo:
    """ um repositorio simples """

    @classmethod
    def insert_user(cls):
        "teste de insercao"
        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name="Programador", password="Lhama")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
            finally:
                db_connection.session.close()
