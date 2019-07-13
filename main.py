from getTweets import *
from analyzeTweets import *
from NLTKTwitterTools import *
from plotTweets import *
from plotCombined import *
from getStockData import *
from analyzeStockData import *
from plotStockData import *
from getLegislatorInfo import *
from runcontrol import controlparameters as cp

##################### Twitter analysis #####################



# ------- extract the legislator infos as a pandas dataframe -------

LC = getLegislatorInfoClass()
legislatorInfo = LC.getInfo()

cp['username'] = legislatorInfo['social__twitter']


# ------- extract the tweets based on some criteria -------
tweets = getTweets(cp,legislatorInfo)
#selectedTweets = tweets.fillTweetList()
#
#
# #------- read in tweets from a file -------
selectedTweets = tweets.readTweetsFromExcelFile('/home/jacob/Dropbox/geekcode/andreas/MLtweets-results-and-whatnot/selectedtweets.csv')

# for tweet in selectedTweets:
#
#     print(tweet.username, tweet.text, tweet.retweets )


## -------  machine learning stuff using NLTK tools -------

NLTKclass = NLTKTwitterToolsClass()
NLTKclass.trainNaiveBayesClassifier()
cat_tweets = NLTKclass.classifyTweets(selectedTweets)

posTweets, negTweets = NLTKclass.splitIntoPosAndNeg(cat_tweets)


# -------  perform some analysis on the selected tweets -------
theAnalysis_pos = analyzeTweets(posTweets)
theAnalysis_pos.populateTimeSeries()
counts_pos = theAnalysis_pos.countNumberOfTweetsPerTime(time='M')

theAnalysis_neg = analyzeTweets(negTweets)
theAnalysis_neg.populateTimeSeries()
counts_neg = theAnalysis_neg.countNumberOfTweetsPerTime(time='M')



# -------  looping over the selected tweets -------
#for tweet in selectedTweets:

#    if "better" in tweet.text:
#        print(tweet.text, tweet.date, tweet.retweets)


# -------  perform some analysis on the selected tweets -------

# plots = plotTweets( dict([('negative tweets', counts_neg), ('positive tweets', counts_pos) ]) )
# plots.makeplot()


##################### Stock data analysis from Yahoo finance #####################


# ------- extract the stock data based on some criteria -------
# stockdata = getStockData()
# ts = stockdata.returnTimeSeries()


#################### get EPS and cashflow data  #################################


FMP = FMPClass()
#FMPdata = FMP.getFMPdata( FQ = 'Free Cash Flow')

FMPdata = FMP.readFMPdataFromCSVfile( FQ = 'Free Cash Flow')

##################### Plotti g for tweets and stockdata #####################

# -------  create some illustrative plots of the selected selected stock data -------

# plots = plotStockData(FMPdata, 'FMT' )
# plots.makeplot()

# -------  create some illustrative plots of the selected selected tweets -------

plots = plotCombined( dict([('negative tweets', counts_neg), ('positive tweets', counts_pos), ('FMPdata', FMPdata) ]) )
plots.makeplot()
