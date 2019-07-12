from runcontrol import controlparameters as cp
import sys,os
import pandas as pd
from tweet import tweet
sys.path.insert(0, cp['pathToTwintModule'])
import twint


class getTweets:

    def __init__(self,cp,legislatorInfo):

        self.cp = cp
        self.legislatorInfo = legislatorInfo
        sys.path.insert(0, self.cp['pathToTwintModule'])
        self.cwd = os.getcwd()
        self.outputcsvfileTwint =  self.cwd + "/" + self.cp['twitterOutputdata'] + "/tweets.csv"



    def removeOldTwintCSVfile(self):

        if os.path.isfile(self.outputcsvfileTwint):
            print("removing old csv output file : " + self.outputcsvfileTwint)
            os.remove(self.outputcsvfileTwint)

        return True

    def fillTweetList(self):

        tweets = []

        if os.path.isfile(self.cp['outputCSVfile']):
            print("removing old csv output file for selected tweets : " + self.cp['outputCSVfile'])
            os.remove(self.cp['outputCSVfile'])
            open(self.cp['outputCSVfile'], "a").close()
        else:
            print("creating csv output file for selected tweets : " + self.cp['outputCSVfile'])
            open(self.cp['outputCSVfile'], "a").close()

        df = pd.DataFrame()
        df_per_user = pd.DataFrame()

        if len(self.cp['username']):

            frames = []
            for i , username in enumerate( self.cp['username'] ):

                frames_per_user = []
                for searchphrase in self.cp['searchphrases']:
                    print("\n****** Getting tweets from legislator: {} (number {}) with the search phrase: {} *******".format(username , i , searchphrase ))
                    self.twintConfig = twint.Config()
                    self.twintConfig.Username = username
                    self.twintConfig.Search = searchphrase
                    self.twintConfig.Store_csv = True
                    self.twintConfig.Limit = self.cp['maxtweets']
                    self.twintConfig.Since = self.cp['startdate']
                    self.twintConfig.Until = self.cp['enddate']
                    self.twintConfig.Custom["tweet"] = ["username", "tweet", "date", "retweets_count"]
                    self.twintConfig.Custom["user"] = ["bio"]
                    self.twintConfig.Output = self.cp['twitterOutputdata']

                    self.removeOldTwintCSVfile()
                    twint.run.Search(self.twintConfig)

                    try:
                        dfram_temp = pd.read_csv( self.outputcsvfileTwint )

                    except FileNotFoundError:
                        print( "\n Info : -------------- No tweets have been found for the legislator {} in the periode "
                               "from {} to {}. Please modify your search critiria --------------- \n".format(username, self.cp['startdate'], self.cp['enddate'] ) )

                    else:

                        for cols in self.legislatorInfo.columns:
                            dfram_temp.insert( len(dfram_temp.columns)  , cols, self.legislatorInfo[cols][i])

                        frames.append(dfram_temp)
                        frames_per_user.append(dfram_temp)

                try:
                    df_per_user = pd.concat(frames)
                except ValueError:
                    pass
                else:

                    df_per_user.sort_values(by=['date'], inplace=True, ascending=True)
                    if len(self.cp['outputCSVfile']): df_per_user.to_csv(self.cp['outputCSVfile'], index=False)

            try:
                df = pd.concat(frames)
            except ValueError:
                pass
            else:
                df.sort_values(by=['date'], inplace=True, ascending=True)


        else:

            print(' Error: ----------- please provide a  list of twitter usernames ---------')
            exit(1)



        for (i, row) in df.iterrows():

            tweetIn = tweet( username = row['username'], text = row['tweet'], date = row['date'] ,
                             retweets = row['retweets_count'], bioguide = row['id__bioguide'] ,
                             legtype =  row['type'], state =  row['state'], party = row['party']  )

            tweets.append(tweetIn)


        return tweets




    def readTweetsFromExcelFile(self,excelfile):

        tweets = []

        df = pd.read_csv(excelfile)

        print(df.columns)

        for (i, row) in df.iterrows():

            tweetIn = tweet( username = row['username'], text = row['tweet'], date = row['date'] ,
                             retweets = row['retweets_count'], bioguide = row['id__bioguide'] ,
                             legtype =  row['type'], state =  row['state'], party = row['party']  )

            tweets.append(tweetIn)

        return self.insertOriginalIndex(tweets)


    def insertOriginalIndex(self,tweets):

        for i, tweet in  enumerate( tweets ):
            tweet.index = i+1

        return tweets

