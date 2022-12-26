import numpy as np
import pandas as pd
import pyupbit
from stockstats import StockDataFrame as Sdf
from Preprocessor import Preprocessor

class UpbitPreprocessor(Preprocessor):
    def __init__(self, ticker, start, end, time_interval, tech_indicator_list):
        super().__init__(start, end, time_interval, tech_indicator_list)
        self.ticker = ticker
        self.ohlcv = pd.DataFrame()

    def download_data(self):
        self.ohlcv = pyupbit.get_ohlcv_from(self.ticker, self.time_interval, self.start, self.end)
    
    def preprocess(self):
        return pd.concat(self.ohlcv, self.ohlcv[self.tech_indicator_list])
    
    def __repr__(self):
        return f'ticker: {self.ticker} | time interval: {self.time_interval} | start/end: {self.start}/{self.end} | indicator: {self.tech_indicator_list}'
        