import logging
from binance.cm_futures import CMFutures as Client
from binance.lib.utils import config_logging
from binance.error import ClientError



class BroBinanceBot:
    
    __binance_client = None
    __config = {}

    def __init__(self, ticker: str, api_key: str, secret_key: str, margin_x: int = 3):
        config_logging(logging, logging.DEBUG)
        self.__binance_client = Client(api_key, secret_key, base_url="https://fapi.binance.com")
        self.__binance_client.change_leverage(ticker, margin_x)
        self.__config["leverage"] = margin_x
        self.__config["ticker"] = ticker

    def set_margin_x(self, x: int) -> None:
        self.__binance_client.change_leverage(self.get_ticker(), x)
        self.__config["leverage"] = x

    def get_margin_x(self) -> int:
        return self.__config["leverage"]

    def get_ticker(self) -> str:
        return self.__config["ticker"]

    

