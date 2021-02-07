import pytest
import pandas as pd
from coinscoin_lib.coinpaprica_synchronize import CoinSynchronize

def test__get_complex_info_about_coin():

    expeted_rank = 1
    expeted_symbol = 'BTC'

    results = CoinSynchronize.get_complex_info_about_coin('btc-bitcoin')
    assert expeted_rank == results.iloc[3][1]
    assert expeted_symbol == results.iloc[2][1]


def test_append_coin_from_list():
    input_list = ['btc-bitcoin', 'ada-cardano']
    df = CoinSynchronize.append_coin_from_list(input_list)
    print(df)


def test_get_coins_df():
    df = CoinSynchronize.get_coins()
    print(df)