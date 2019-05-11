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
        self.outputcsvfileTwint =  self.cwd + "/" + cp['twitterOutputdata'] + "/tweets.csv"


    def removeOldTwintCSVfile(self):

        if os.path.isfile(self.outputcsvfileTwint):
            print("removing old csv output file : " + self.outputcsvfileTwint)
            os.remove(self.outputcsvfileTwint)

        return True

    def fillTweetList(self):

        tweets = []

        if os.path.isfile(cp['outputCSVfile']):
            print("removing old csv output file for selected tweets : " + cp['outputCSVfile'])
            os.remove(cp['outputCSVfile'])
            open(cp['outputCSVfile'], "w+").close()
        else:
            print("creating csv output file for selected tweets : " + cp['outputCSVfile'])
            open(cp['outputCSVfile'], "w+").close()

        df = pd.DataFrame()

        if len(cp['username']):

            frames = []
            for username in cp['username']:
                self.twintConfig = twint.Config()
                self.twintConfig.Username = username
                self.twintConfig.Search = cp['searchphrase']
                self.twintConfig.Store_csv = True
                self.twintConfig.Limit = cp['maxtweets']
                self.twintConfig.Since = cp['startdate']
                self.twintConfig.Until = cp['enddate']
                self.twintConfig.Custom["tweet"] = ["username", "tweet", "date", "retweets_count"]
                self.twintConfig.Custom["user"] = ["bio"]
                self.twintConfig.Output = cp['twitterOutputdata']

                self.removeOldTwintCSVfile()

                twint.run.Search(self.twintConfig)

                frames.append( pd.read_csv(self.outputcsvfileTwint) )

            df = pd.concat(frames)
            df.sort_values(by=['date'], inplace=True, ascending=True)
            if len(cp['outputCSVfile']): df.to_csv(cp['outputCSVfile'], index=False)
            print(df)

        else:
            self.twintConfig = twint.Config()
            self.twintConfig.Search = cp['searchphrase']
            self.twintConfig.Store_csv = True
            self.twintConfig.Limit = cp['maxtweets']
            self.twintConfig.Since = cp['startdate']
            self.twintConfig.Until = cp['enddate']
            self.twintConfig.Custom["tweet"] = ["username", "tweet", "date", "retweets_count"]
            self.twintConfig.Custom["user"] = ["bio"]
            self.twintConfig.Output = cp['twitterOutputdata']

            self.removeOldTwintCSVfile()
            twint.run.Search(self.twintConfig)
            df = pd.read_csv(self.outputcsvfileTwint)

        for (i, row) in df.iterrows():

            tweetIn = tweet( username = row['username'], text = row['tweet'], date = row['date'] , retweets = row['retweets_count'])

            tweets.append(tweetIn)



        return tweets




    def readTweetsFromExcelFile(self,excelfile):

        tweets = []

        df = pd.read_csv(self.outputcsvfileTwint)

        for (i, row) in df.iterrows():

            tweetIn = tweet( username = row['username'], text = row['tweet'], date = row['date'] , retweets = row['retweets_count'])

            tweets.append(tweetIn)

        return self.insertOriginalIndex(tweets)


    def insertOriginalIndex(self,tweets):

        for i, tweet in  enumerate( tweets ):
            tweet.index = i+1

        return tweets

