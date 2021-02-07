from coinscoin_lib.coinpaprica_synchronize import CoinSynchronize
from coinscoin_lib.resource_manager import ResourceManager


class DataDump:

    def __init__(self, process_run_key: int = None):
        # Input params
        self.process_run_key = process_run_key
        self.db_session = ResourceManager.db_session()

    @staticmethod
    def run_data_dump_master():
        CoinSynchronize.handle()

