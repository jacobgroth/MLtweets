from getTweets import *
from writeTweets import *
from analyzeTweets import *
from NLTKTwitterTools import *
from plotTweets import *
from getStockData import *
from analyzeStockData import *
from plotStockData import *


##################### Twitter analysis #####################

# ------- extract the tweets based on some criteria -------
tweets = getTweets()
#selectedTweets = tweets.GetTheLastNTweetsByUsernameAndBoundDatesByQuerySearch()
#print(selectedTweets)
# ------- read in tweets from a file -------
selectedTweets = tweets.readTweetsFromExcelFile('output.xlsx')


# -------  if you want to write the tweets to a CSV file -------
#writetweets = writeTweets(selectedTweets)
#writetweets.writeTweetsToCSVFile()

# -------  machine learning stuff using NLTK tools -------

NLTKclass = NLTKTwitterToolsClass()
NLTKclass.trainNaiveBayesClassifier()
cat_tweets = NLTKclass.classifyTweets(selectedTweets)

posTweets, negTweets = NLTKclass.splitIntoPosAndNeg(cat_tweets)


# -------  perform some analysis on the selected tweets -------
theAnalysis_pos = analyzeTweets(posTweets)
theAnalysis_pos.populateTimeSeries()
counts_pos = theAnalysis_pos.countNumberOfTweetsPerTime()

theAnalysis_neg = analyzeTweets(negTweets)
theAnalysis_neg.populateTimeSeries()
counts_neg = theAnalysis_neg.countNumberOfTweetsPerTime()



# -------  looping over the selected tweets -------
#for tweet in selectedTweets:

#    if "better" in tweet.text:
#        print(tweet.text, tweet.date, tweet.retweets)



##################### Stock data analysis #####################


# ------- extract the stock data based on some criteria -------
stockdata = getStockData()
ts = stockdata.returnTimeSeries()['Close']



# -------  perform some analysis on the selected tweets -------



##################### Plotti g for tweets and stockdata #####################

# -------  create some illustrative plots of the selected selected stock data -------

#plots = plotStockData(ts)
#plots.makeplot()

# -------  create some illustrative plots of the selected selected tweets -------
plots = plotTweets( dict([('negative tweets', counts_neg), ('positive tweets', counts_pos), ('Stock Rate : MSFT', ts) ]) )
plots.makeplot()
