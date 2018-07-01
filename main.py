from helperClasses import *


# ------- extract the tweets based on some criteria -------
tweets = getTweets()
selectedTweets = tweets.GetTweetsByQuerySearch()


# -------  perform some analysis on the selected tweets -------
theAnalysis = analyzeTweets(selectedTweets)
theAnalysis.populateTimeSeries()
counts = theAnalysis.countNumberOfTweetsPerTime()



# -------  if you want to write the tweets to a CSV file -------
#writetweets = writeTweets(selectedTweets)
#writetweets.writeTweetsToCSVFile()

# -------  looping over the selected tweets -------
#for tweet in selectedTweets:

#    if "better" in tweet.text:
#        print(tweet.text, tweet.date, tweet.retweets)


# -------  create some illustrative plots of the selected selected tweets -------
plots = plotTweets(counts)
plots.makeplot()


