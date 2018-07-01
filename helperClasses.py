from runcontrol import controlparameters as cp
import sys
import csv
import numpy as np
import pandas as pd
import seaborn; seaborn.set()
import matplotlib.pyplot as plt


class getTweets:

    def __init__(self):
        sys.path.insert(0, cp['pathToGetOldTweetsModule'])
        import got3
        self.Got3Manager = got3.manager


    def GetTweetsByUsername(self):
        tweetCriteria = self.Got3Manager.TweetCriteria().setUsername(cp['username']).setMaxTweets(cp['maxtweets'])
        tweet = self.Got3Manager.TweetManager.getTweets(tweetCriteria)[0]
        return tweet


    def GetTweetsByQuerySearch(self,text=None):

        if text==None:
            text = cp['searchphrase']

        tweetCriteria = self.Got3Manager.TweetCriteria().setQuerySearch(text).setSince(cp['startdate']).setUntil(cp['enddate']).setMaxTweets(cp['maxtweets'])
        tweet = self.Got3Manager.TweetManager.getTweets(tweetCriteria)
        return tweet

    def GetTweetsByUsernameAndBoundDates(self):
        tweetCriteria = self.Got3Manager.TweetCriteria().setUsername(cp['username']).setSince(cp['startdate']).setUntil(cp['enddate']).setMaxTweets(cp['maxtweets'])
        tweet = self.Got3Manager.TweetManager.getTweets(tweetCriteria)
        return tweet

    def GetTheLastNTopTweetsByUsername(self,number=None):

        if number==None:
            number = cp['maxtweets']

        tweetCriteria = self.Got3Manager.TweetCriteria().setUsername(cp['username']).setTopTweets(True).setMaxTweets(number)
        tweet = self.Got3Manager.TweetManager.getTweets(tweetCriteria)
        return tweet


class writeTweets:

    def __init__(self,tweets):
        self.tweets = tweets

    def setTweets(self,tweets):
        self.tweets = tweets

    def writeTweetsToCSVFile(self):

        with open('tweets.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=';',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)

            for tweet in self.tweets:

                csvwriter.writerow([ tweet.username, tweet.retweets  , tweet.text  ,  tweet.date])


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
            retweets.append(tweet.retweets)

        index = pd.DatetimeIndex(dates)
        data = pd.Series(retweets, index=index)

        data.columns = ['retweets']

        self.data = data



    def countNumberOfTweetsPerTime(self,time='H'):

        counts = self.data.groupby([self.data.index.day,self.data.index.hour]).count()

        return counts



class plotTweets:

    def __init__(self,dataset):
        self.dataset = dataset

        print(self.dataset)

    def makeplot(self):

        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.set_xlabel('date')
        ax1.set_ylabel('number of tweets')
        ax1.set_title("number of time a tweet contains the phase: {}".format(cp['searchphrase']))
        self.dataset.plot(style="o-")
        plt.legend(['data'], loc='upper left');

        plt.show()