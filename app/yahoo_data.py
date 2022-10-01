from datetime import datetime
from typing import Dict, Tuple
import yfinance as yf

import pandas as pd

class YahooData:

    @staticmethod
    def get_all_market_data(ticker: str) -> pd.DataFrame:


        msft = yf.Ticker(ticker)

        # get historical market data
        hist = msft.history(interval="1d",period="max")

        hist['date'] = pd.to_datetime(hist.index)

        print(hist)

        print(hist["Open"][0])

        print(len(hist))

        print(hist.index[0])

        #print(hist)

        return hist


    @staticmethod
    def get_latest_market_data_price(symbol: str) -> Dict:

        msft = yf.Ticker(symbol)

        symbol_data = {}

        symbol_data['datetime'] =  datetime.now()

        symbol_data['symbol'] = symbol

        symbol_data['price'] = msft.info['regularMarketPrice']

        symbol_data['currency'] = msft.info['currency']

        prices = []

        prices.append(symbol_data)

        print(msft.info)

        return prices

    @staticmethod
    def get_market_data_price(ticker: str, point_in_time: datetime) -> float:


        msft = yf.Ticker(ticker)

        price = msft.info['regularMarketPrice']

        return price
    

#df: pd.DataFrame = YahooData.get_market_data("MSFT")
#print (df.to_sql)