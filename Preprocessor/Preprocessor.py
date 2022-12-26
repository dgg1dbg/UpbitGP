class Preprocessor:
    def __init__(self, start, end, time_interval, tech_indicator_list):
        self.start = start
        self.end = end
        self.time_interval = time_interval
        self.tech_indicator_list = tech_indicator_list

    def download_data(self):
        pass

    def preprocess(self):
        pass

    def __repr__(self):
        pass