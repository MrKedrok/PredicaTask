import sqlalchemy
from sqlalchemy.orm.session import sessionmaker, Session
from skidservice_lib.postgres_session import PostgresSession
import re


class PostgresConnectionParameters:
    connection_string: str

    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        proto, _, user, _, passwd, host, _, db_name = re.search(
            '(.+://)?((.+(@.+)?):(.+))?@(.+)(:\d+)?/(.+)',
            connection_string
        ).groups()

        self.username = user
        self.password = passwd
        self.hostname = host
        self.database = db_name

    def __str__(self):
        return self.__connection_string

    @property
    def jdbc_connection_string(self):
        return f'jdbc:postgresql://{self.hostname}:5432/{self.database}'


class Database:
    def __init__(self, connection_string: str):
        self.session_maker = sessionmaker()
        self.__db_engine = sqlalchemy.create_engine(
            connection_string
        )
        self.session_maker.configure(bind=self.__db_engine)

    def get_sa_session(self) -> Session:
        return self.session_maker()

    def get_session(self) -> PostgresSession:
        return PostgresSession(self.get_sa_session())
