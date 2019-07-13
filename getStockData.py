from pandas_datareader import data as pdr
from runcontrol import controlparameters as cp
import fix_yahoo_finance as yf
import json
import pandas as pd
import time

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

        self.listOfCompShort = self.populateListOfCompanyUrls()

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

        time.sleep(1)
        response = urlopen(url)
        data = response.read().decode("utf-8")
        return json.loads(data)


    def formatFMPdata(self, FQ = 'EPS'):

        FQkeyWord = ''

        if FQ == 'EPS':
            FQkeyWord = 'income-statement'
        #elif FQ == 'Free Cash Flow':
        elif FQ == 'Free Cash Flow':
            FQkeyWord = 'cash-flow-statement'


        dataFrameDict = {}
        index = []

        for i, comp in enumerate( self.listOfCompShort ):

            url = (self.baseUrl + FQkeyWord + '/' +comp  + self.period )
            print(comp, i)
            compdataDict = self.retriveRawFMPdata(url)
            FQdata = []

            try:
                compdataDict['financials']
            except:
                print( "THere is no financial information about company {} - skipping this company".format(comp) )
                pass
            else:
                for FS in compdataDict['financials']:
                    if FS['date'] < cp['startdate'] or FS['date'] > cp['enddate'] : continue
                    try:
                        float(FS[FQ])
                    except ValueError:
                        print(" ValueError while extracting financial data. Inserting 0. Place take that into account ")
                        FQdata.append(0.0)
                    else:
                        FQdata.append( float(FS[FQ]) )
                    if i == 0: index.append(FS['date'])

            if len(FQdata) != len(index): continue
            dataFrameDict[ comp ] = FQdata
            index = pd.DatetimeIndex(index)

        return pd.DataFrame(data=dataFrameDict, index = index)


    def getFMPdata(self, FQ = 'ESP', avg = True  ):

        """
        Det the FMP data and populates a pandas time series with the average value of the information .
        Also writes the non-averaged information to a CSV file
        :param FQ:
        :param avg:
        :return:
        """

        timeSeriesData = self.formatFMPdata(FQ = FQ)
        print(timeSeriesData)

        outputCVSfilename = cp['companyInfoDir'] + FQ.replace(" ", "") + '_' +  cp['FMPdataoutputfileCSV']

        open( outputCVSfilename  , "w+").close()
        timeSeriesData.to_csv( outputCVSfilename )

        if avg == True:
            timeSeriesData = timeSeriesData.mean(axis = 1)
            timeSeriesData = pd.Series( timeSeriesData )

        return timeSeriesData

    def populateListOfCompanyUrls(self):

        comInfo = pd.read_csv( cp['companyInfoDir'] + cp['SandP500file'] , sep=';')

        return [str(short) for short in comInfo['ticker']]


    def readFMPdataFromCSVfile(self , FQ = 'ESP' , filter = True , avg = True ):

        FMPdata = pd.read_csv( cp['companyInfoDir'] + FQ.replace(" ", "") + '_' +  cp['FMPdataoutputfileCSV']  )

        if filter == False : return FMPdata

        comInfo_DataFrame = pd.read_csv(cp['companyInfoDir'] + cp['SandP500file'], sep=';')

        index =  pd.DatetimeIndex( FMPdata['Unnamed: 0'] )
        FMPdata.index = index
        FMPdata.drop(columns='Unnamed: 0')

        for comp in FMPdata.columns:
            if comp == 'Unnamed: 0':continue

            sector = str( comInfo_DataFrame.loc[ comInfo_DataFrame['ticker'] == comp , 'GICS_sector' ].iat[0] )

            if sector not in cp['companySector']: FMPdata.pop( comp )

        FMPdata.pop('Unnamed: 0')
        FMPdata.index.name = 'date'
        if avg == True: FMPdata = FMPdata.mean(axis=1)
        return FMPdata

