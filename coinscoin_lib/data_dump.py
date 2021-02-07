import logging as log

from pandas import DataFrame
from coinscoin_lib import coinpaprica_synchronize as data


class DataDump:

    def __init__(self, process_run_key: int = None):
        # Input params
        self.process_run_key = process_run_key

    @staticmethod
    def run_data_dump_master():
        data.CoinSynchronize.handle()
