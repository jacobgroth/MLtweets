from getTweets import *
from writeTweets import *
from analyzeTweets import *
from plotTweets import *
from getStockData import *
from analyzeStockData import *
from plotStockData import *


##################### Twitter analysis #####################

# ------- extract the tweets based on some criteria -------
#tweets = getTweets()
#selectedTweets = tweets.GetTheLastNTweetsByUsernameAndBoundDatesByQuerySearch()

# ------- read in tweets from a file -------
#selectedTweets = tweets.readTweetsFromExcelFile('output.xlsx')


# -------  if you want to write the tweets to a CSV file -------
#writetweets = writeTweets(selectedTweets)
#writetweets.writeTweetsToCSVFile()


# -------  perform some analysis on the selected tweets -------
#theAnalysis = analyzeTweets(selectedTweets)
#theAnalysis.populateTimeSeries()
#counts = theAnalysis.countNumberOfTweetsPerTime()


# -------  looping over the selected tweets -------
#for tweet in selectedTweets:

#    if "better" in tweet.text:
#        print(tweet.text, tweet.date, tweet.retweets)


# -------  create some illustrative plots of the selected selected tweets -------
#plots = plotTweets(counts)
#plots.makeplot()



##################### Stock data analysis #####################


# ------- extract the stock data based on some criteria -------
stockdata = getStockData()
ts = stockdata.returnTimeSeries()

# -------  perform some analysis on the selected tweets -------


# -------  create some illustrative plots of the selected selected stock data -------

plots = plotStockData(ts)
plots.makeplot()