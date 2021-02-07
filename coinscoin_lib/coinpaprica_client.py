from coinpaprika import client as coinpaprika


class ApiClient:

    def __init__(self):
        self.client_maker = coinpaprika.Client()

    @staticmethod
    def get_session() -> coinpaprika:
        return coinpaprika.Client()

    @staticmethod
    def get_coinpaprica_coin_info(input_id: str) -> dict:
        """
        # Get coin by ID (example: btc-bitcoin)
        :param: input_id str
        :return: dict
        """
        return ApiClient.get_session().coin(input_id)

    @staticmethod
    def get_coinpaprica_events(input_id: str) -> list:
        """
        # Get coin by ID (example: btc-bitcoin)
        :param: input_id
        :return:
        """
        return ApiClient.get_session().events(input_id)

    @staticmethod
    def get_coinpaprica_candles(input_id: str) -> list:
        """
        # Get coin by ID (example: btc-bitcoin)
        :param: input_id
        :return:
        """
        return ApiClient.get_session().candles(input_id)

    @staticmethod
    def get_coinpaprica_today(input_id: str) -> list:
        """
        # Get coin by ID (example: btc-bitcoin)
        :param: input_id
        :return:
        """
        return ApiClient.get_session().today(input_id)

    @staticmethod
    def get_coinpaprica_coins() -> list:
        """
        # Get coin by ID (example: btc-bitcoin)
        :param: input_id
        :return:
        """
        return ApiClient.get_session().coins()
