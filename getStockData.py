from pandas_datareader import data as pdr
from runcontrol import controlparameters as cp
import fix_yahoo_finance as yf
import json
import pandas as pd

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


class getStockData:

    def __init__(self):
        yf.pdr_override()

    def returnTimeSeries(self):

        data = pdr.get_data_yahoo(cp['stockindex'], start=cp["startdate"], end=cp["enddate"])

        return data


class FMPClass:

    def __init__(self ):

        self.baseUrl = 'https://financialmodelingprep.com/api/v3/financials/'
        self.period = '?period=quarter'
        self.datatype = ''
        #self.datatype = '?datatype=json'

        self.listOfCompShort = self.populateListOfCompanyUrls(top = 25)

    def retriveRawFMPdata(self, url):
        """
        Receive the content of ``url``, parse it as JSON and return the object.

        Parameters
        ----------
        url : str

        Returns
        -------
        dict
        """
        response = urlopen(url)
        data = response.read().decode("utf-8")
        return json.loads(data)


    def formatFMPdata(self, FQ = 'EPS'):

        FQkeyWord = ''

        if FQ == 'EPS':
            FQkeyWord = 'income-statement'
        elif FQ == 'Free Cash Flow':
            FQkeyWord = 'cash-flow-statement'


        dataFrameDict = {}
        index = []

        for i, comp in enumerate( self.listOfCompShort ):

            url = (self.baseUrl + FQkeyWord + '/' +comp  + self.period )
            print(comp, i)
            compdataDict = self.retriveRawFMPdata(url)
            FQdata = []

            for FS in compdataDict['financials']:
                if FS['date'] < cp['startdate'] or FS['date'] > cp['enddate'] : continue
                FQdata.append( float(FS[FQ]) )
                if i == 0: index.append(FS['date'])

            dataFrameDict[ comp ] = FQdata
            index = pd.DatetimeIndex(index)

        return pd.DataFrame(data=dataFrameDict, index = index)




    def getFMPdata(self, FQ = 'ESP', avg = True):


        timeSeriesData = self.formatFMPdata(FQ = FQ)
        print(timeSeriesData)

        if avg == True:
            timeSeriesData = timeSeriesData.mean(axis = 1)
            timeSeriesData = pd. Series( timeSeriesData )

        return timeSeriesData

    def populateListOfCompanyUrls(self, top = 100):

        comInfo = pd.read_csv( cp['companyInfoDir'] + "SP100_list.csv" )

        return [str(short) for short in comInfo['ticker']][:top]


