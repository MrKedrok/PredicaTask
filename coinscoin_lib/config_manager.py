from coinscoin_lib.config import Config
import logging as log
import os
import configparser


class ConfigManager:
    __current_config = None

    def __init__(self):
        raise Exception('don''t use it that way')

    @staticmethod
    def __get_from_file(filename):
        config = configparser.ConfigParser()
        config.read(filename)
        main_section = config['main']
        return Config(
            scope_of_data_to_analyze=main_section["scope_of_data_to_analyze"],
            data_dump_task=main_section["data_dump_task"],
            internal_redis_connection_string=main_section["internal_redis_connection_string"]

        )

    @staticmethod
    def init_test():
        log.debug("initializing test configuration")
        ConfigManager.__current_config = ConfigManager.get_config()

    @staticmethod
    def init_with_file(filename):
        ConfigManager.__current_config = ConfigManager.__get_from_file(filename)

    @staticmethod
    def initialize():
        config_file = os.getenv('COINSCOIN_CONFIG', '/opt/PredicaTask/etc/skidservice.conf')
        ConfigManager.init_with_file(config_file)

    @staticmethod
    def get_config() -> Config:
        ConfigManager.initialize()
        return ConfigManager.__current_config
