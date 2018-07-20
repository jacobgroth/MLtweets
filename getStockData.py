from pandas_datareader import data as pdr
from runcontrol import controlparameters as cp
import fix_yahoo_finance as yf

class getStockData:

    def __init__(self):
        yf.pdr_override()

    def returnTimeSeries(self):

        data = pdr.get_data_yahoo("MSFT", start=cp["startdate"], end=cp["enddate"])

        return data