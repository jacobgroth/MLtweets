import pandas as pd

class analyzeTweets:

    def __init__(self,tweets):
        self.tweets = tweets

    def setTweets(self,tweets):
        self.tweets = tweets

    def populateTimeSeries(self):

        dates = []
        retweets = []

        for tweet in self.tweets:

            dates.append(tweet.date)
            retweets.append(tweet.retweets+1)

        index = pd.DatetimeIndex(dates)
        data = pd.Series(retweets, index=index)

        data.columns = ['retweets']

        self.data = data



    def countNumberOfTweetsPerTime(self,time='H'):

        #counts = self.data.groupby([self.data.index.year,self.data.index.month,self.data.index.day,self.data.index.hour]).count()
        counts = self.data.resample(time).count()


        return counts


