from coinscoin_lib import coinpaprica_client as coinpaprica
from coinscoin_lib.config_manager import ConfigManager
import pandas as pd
from datetime import datetime

#scope_of_data_to_analyze = int(ConfigManager.get_config().scope_of_data_to_analyze)
scope_of_data_to_analyze = 100

class CoinSynchronize:

    def __init__(self):
        self.coins = coinpaprica.ApiClient()
        pass

    @staticmethod
    def get_complex_info_about_coin(input_coin_id: str) -> pd.DataFrame:
        dict_coin = coinpaprica.ApiClient().get_coinpaprica_coin_info(input_coin_id)
        pd_df = pd.DataFrame(list(dict_coin.items()))
        return pd_df

    @staticmethod
    def get_current_value_coin(input_coin_id: str) -> pd.DataFrame:
        dict_coin = coinpaprica.ApiClient().get_coinpaprica_today(input_coin_id)
        pd_df = pd.DataFrame(list(dict_coin))
        return pd_df

    @staticmethod
    def get_coins_id() -> pd.DataFrame:
        dict_coin = coinpaprica.ApiClient().get_coinpaprica_coins()
        pd_df = pd.DataFrame(list(dict_coin))["id"]
        return pd_df

    @staticmethod
    def get_daily_data() -> pd.DataFrame:
        data_you_need = pd.DataFrame()
        for id in CoinSynchronize.get_coins_id().head(scope_of_data_to_analyze):
            data = CoinSynchronize.get_current_value_coin(id)
            data_you_need = data_you_need.append(data, ignore_index=True)
        added_id_to_df = pd.concat([data_you_need, CoinSynchronize.get_coins_id().head(scope_of_data_to_analyze)], axis=1)
        return added_id_to_df

    @staticmethod
    def append_coin_from_list(input_list: list) -> pd.DataFrame:
        df1 = CoinSynchronize.get_current_value_coin(input_list[1])
        df2 = CoinSynchronize.get_current_value_coin(input_list[0])
        df = df1.append(df2)
        return df

    @staticmethod
    def handle():
        Coins_incremental_data = CoinSynchronize.get_daily_data()
        Coins_incremental_data.to_csv('daily_dump_'+str(round(int(str(datetime.today().strftime("%M%S%f"))) / 100))+'.csv', index=False)
