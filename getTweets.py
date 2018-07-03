from runcontrol import controlparameters as cp
import sys
import pandas as pd

class getTweets:

    def __init__(self):
        sys.path.insert(0, cp['pathToGetOldTweetsModule'])
        import got3
        self.Got3Manager = got3.manager

    def GetTweetsByUsername(self):
        tweetCriteria = self.Got3Manager.TweetCriteria().setUsername(cp['username']).setMaxTweets(cp['maxtweets'])
        tweets = self.Got3Manager.TweetManager.getTweets(tweetCriteria)[0]
        return tweets


    def GetTweetsByQuerySearch(self,text=None):

        if text==None:
            text = cp['searchphrase']

        tweetCriteria = self.Got3Manager.TweetCriteria().setQuerySearch(text).setSince(cp['startdate']).setUntil(cp['enddate']).setMaxTweets(cp['maxtweets'])
        tweets = self.Got3Manager.TweetManager.getTweets(tweetCriteria)
        return tweets

    def GetTweetsByUsernameAndBoundDates(self):
        tweetCriteria = self.Got3Manager.TweetCriteria().setUsername(cp['username']).setSince(cp['startdate']).setUntil(cp['enddate']).setMaxTweets(cp['maxtweets'])
        tweets = self.Got3Manager.TweetManager.getTweets(tweetCriteria)
        return tweets

    def GetTheLastNTopTweetsByUsername(self,number=None):

        if number==None:
            number = cp['maxtweets']

        tweetCriteria = self.Got3Manager.TweetCriteria().setUsername(cp['username']).setTopTweets(True).setMaxTweets(number)
        tweets = self.Got3Manager.TweetManager.getTweets(tweetCriteria)
        return tweets

    def GetTheLastNTopTweetsByUsernameAndBoundDates(self,number=None):

        if number==None:
            number = cp['maxtweets']

        tweetCriteria = self.Got3Manager.TweetCriteria().setUsername(cp['username']).setSince(cp['startdate']).setUntil(cp['enddate']).setTopTweets(True).setMaxTweets(number)
        tweets = self.Got3Manager.TweetManager.getTweets(tweetCriteria)
        return tweets

    def GetTheLastNTweetsByUsernameAndBoundDates(self,number=None):

        if number==None:
            number = cp['maxtweets']

        tweetCriteria = self.Got3Manager.TweetCriteria().setUsername(cp['username']).setSince(cp['startdate']).setUntil(cp['enddate']).setMaxTweets(number)
        tweets = self.Got3Manager.TweetManager.getTweets(tweetCriteria)
        return tweets

    def GetTheLastNTopTweetsByUsernameAndBoundDatesByQuerySearch(self,number=None,text=None):

        if number==None:
            number = cp['maxtweets']

        if text==None:
            text = cp['searchphrase']

        tweetCriteria = self.Got3Manager.TweetCriteria().setQuerySearch(text).setUsername(cp['username']).setSince(cp['startdate']).setUntil(cp['enddate']).setTopTweets(True).setMaxTweets(number)
        tweets = self.Got3Manager.TweetManager.getTweets(tweetCriteria)
        return tweets

    def GetTheLastNTweetsByUsernameAndBoundDatesByQuerySearch(self,number=None,text=None):

        if number==None:
            number = cp['maxtweets']

        if text==None:
            text = cp['searchphrase']

        tweetCriteria = self.Got3Manager.TweetCriteria().setQuerySearch(text).setSince(cp['startdate']).setUntil(cp['enddate']).setMaxTweets(number)
        tweets = self.Got3Manager.TweetManager.getTweets(tweetCriteria)
        return tweets

    def readTweetsFromExcelFile(self,excelfile):

        from got3 import models
        df = pd.read_excel(excelfile)

        tweets = []

        for index, row in df.iterrows():
            tweet = models.Tweet()

            tweet.id = row['id']
            tweet.permalink = '0'
            tweet.username = row['username']
            tweet.text = row['text']
            tweet.date = index
            tweet.retweets = row['retweets']
            tweet.favorites  = row['favorites']
            tweet.mentions = row['mentions']
            tweet.hashtags  = row['hashtags']
            tweet.geo  = '0'

            tweets.append(tweet)

        return tweets



