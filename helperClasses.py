from runcontrol import controlparameters as cp
import sys


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

    def GetTheLast10TopTweetsByUsername(self,number=None):

        if number==None:
            number = cp['maxtweets']

        tweetCriteria = self.Got3Manager.TweetCriteria().setUsername(cp['username']).setTopTweets(True).setMaxTweets(number)
        tweet = self.Got3Manager.TweetManager.getTweets(tweetCriteria)
        return tweet
