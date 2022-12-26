from UpbitPreprocessor import UpbitPreprocessor

setting = {'ticker': 'KRW-BTC', 'start': '20201010', 'end': '20201012', 'time_interval': 'min60', 'tech_indicator_list': ['boll', 'macd']}
up = UpbitPreprocessor(**setting)
up.download_data()
print(up.preprocess())
print(up)