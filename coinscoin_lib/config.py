

class Config:
    __config_dict = {}

    def __init__(self,
                 scope_of_data_to_analyze: int,
                 data_dump_task: int,
                 internal_redis_connection_string: str,
                 mssql_connection: str):
        """

        """

        self.scope_of_data_to_analyze = scope_of_data_to_analyze
        self.data_dump_task = data_dump_task
        self.internal_redis_connection_string = internal_redis_connection_string
        self.mssql_connection = mssql_connection
