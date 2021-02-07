from urllib.parse import urlparse
from coinscoin_lib.config_manager import ConfigManager
from coinscoin_lib.database import Database
from coinscoin_lib.msql_session import MSSQLSession


class ResourceManager:
    __database = None
    __redis = None

    def __init__(self):
        raise Exception('don''t use it that way')

    @staticmethod
    def database():
        if not ResourceManager.__database:
            ResourceManager.__database = Database(
                connection_string=ConfigManager.get_config().mssql_connection)
        return ResourceManager.__database

    @staticmethod
    def db_session() -> MSSQLSession:
        return ResourceManager.database().get_session()


