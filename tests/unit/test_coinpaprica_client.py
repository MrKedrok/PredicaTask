import pytest
import pandas as pd
from coinscoin_lib.coinpaprica_client import ApiClient

def test_get_coinpaprica_coin_info():
    expeted_rank = 1
    expeted_symbol = 'BTC'

    results = ApiClient.get_coinpaprica_coin_info("btc-bitcoin")
    pd_results = pd.DataFrame(list(results.items()))
    assert expeted_rank == pd_results.iloc[3][1]
    assert expeted_symbol == pd_results.iloc[2][1]

