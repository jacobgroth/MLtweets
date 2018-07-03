from alpha_vantage.timeseries import TimeSeries
from runcontrol import controlparameters as cp

class getStockData:

    def __init__(self):

        self.ts = TimeSeries(key=cp['AVAPI'], output_format='pandas')


    def returnTimeSeries(self):

        data, meta_data = self.ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')

        return data