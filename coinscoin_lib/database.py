import sqlalchemy
from sqlalchemy.orm.session import sessionmaker, Session
from coinscoin_lib.msql_session import MSSQLSession


class Database:
    def __init__(self, connection_string: str):
        self.session_maker = sessionmaker()
        self.__db_engine = sqlalchemy.create_engine(
            connection_string
        )
        self.session_maker.configure(bind=self.__db_engine)

    def get_sa_session(self) -> Session:
        return self.session_maker()

    def get_session(self) -> MSSQLSession:
        return MSSQLSession(self.get_sa_session())
