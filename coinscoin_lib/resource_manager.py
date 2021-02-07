from urllib.parse import urlparse
from coinscoin_lib.config_manager import ConfigManager
from coinscoin_lib.database import Database
from coinscoin_lib.postgres_session import PostgresSession


class ResourceManager:
    __database = None
    __redis_cache = None
    __internal_redis = None
    __spark_ops = None

    def __init__(self):
        raise Exception('don''t use it that way')

    @staticmethod
    def database():
        if not ResourceManager.__database:
            ResourceManager.__database = Database(
                connection_string=ConfigManager.get_config().postgresql_connection_string)
        return ResourceManager.__database

    @staticmethod
    def db_session() -> PostgresSession:
        return ResourceManager.database().get_session()
    @staticmethod
    def db_session() -> PostgresSession:
        return ResourceManager.database().get_session()

