from runcontrol import controlparameters as cp
import sys,os
import pandas as pd
from tweet import tweet
sys.path.insert(0, cp['pathToTwintModule'])
import twint


class getTweets:

    def __init__(self):
        sys.path.insert(0, cp['pathToTwintModule'])
        self.cwd = os.getcwd()
        self.outputcsvfile =  self.cwd + "/" + cp['twitterOutputdata'] + "/tweets.csv"

        self.twintConfig = twint.Config()



    def fillTweetList(self):

        tweets = []

        if os.path.isfile(self.outputcsvfile):
            print("removing old csv output file : " + self.outputcsvfile)
            os.remove(self.outputcsvfile)


        if len(cp['username']): self.twintConfig.Username = cp['username']
        self.twintConfig.Search = cp['searchphrase']
        self.twintConfig.Store_csv = True
        self.twintConfig.Limit = cp['maxtweets']
        self.twintConfig.Since =  cp['startdate']
        self.twintConfig.Until =  cp['enddate']
        self.twintConfig.Custom["tweet"] = ["username","tweet","date", "retweets_count"]
        self.twintConfig.Custom["user"] = ["bio"]
        self.twintConfig.Output = cp['twitterOutputdata']

        twint.run.Search(self.twintConfig)

        df = pd.read_csv(self.outputcsvfile)

        for (i, row) in df.iterrows():

            tweetIn = tweet( username = row['username'], text = row['tweet'], date = row['date'] , retweets = row['retweets_count'])

            tweets.append(tweetIn)

        return tweets




    def readTweetsFromExcelFile(self,excelfile):

        tweets = []

        df = pd.read_csv(self.outputcsvfile)

        for (i, row) in df.iterrows():

            tweetIn = tweet( username = row['username'], text = row['tweet'], date = row['date'] , retweets = row['retweets_count'])

            tweets.append(tweetIn)

        return self.insertOriginalIndex(tweets)


    def insertOriginalIndex(self,tweets):

        for i, tweet in  enumerate( tweets ):
            tweet.index = i+1

        return tweets

