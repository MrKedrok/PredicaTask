import os

TEST_ROOT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tests')
TEST_DATA_ROOT = os.path.join(TEST_ROOT_PATH, 'data')
TEST_TMP_ROOT = '/tmp'
TEST_SHARED_ROOT = '/mnt/sharedvolume'


class Config:
    __config_dict = {}

    def __init__(self,
                 scope_of_data_to_analyze: int,
                 data_dump_task: int,
                 internal_redis_connection_string: str):
        """

        """

        self.scope_of_data_to_analyze = scope_of_data_to_analyze
        self.data_dump_task = data_dump_task
        self.internal_redis_connection_string = internal_redis_connection_string
