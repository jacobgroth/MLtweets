import pandas as pd


class writeTweets:

    def __init__(self,tweets):
        self.tweets = tweets

    def setTweets(self,tweets):
        self.tweets = tweets

    def writeTweetsToCSVFile(self):

        id, permalink, username, text, date, retweets, favorites, mentions, hashtags, geo =  [], [], [], [], [], [], [], [], [], []

        for tweet in self.tweets:

            id.append(tweet.id)
            permalink.append('0')
            username.append(tweet.username)
            text.append(tweet.text)
            date.append(tweet.date)
            retweets.append(tweet.retweets)
            favorites.append(tweet.favorites)
            mentions.append(tweet.mentions)
            hashtags.append(tweet.hashtags)
            geo.append('0')

        dataDict = { 'id' : id , 'permalink ' : permalink, 'username' : username,
                     'text' : text, 'retweets' : retweets, 'favorites' : favorites,
                     'mentions' : mentions, 'hashtags' : hashtags, 'geo ' : geo }

        df = pd.DataFrame(dataDict, index=date)

        writer = pd.ExcelWriter('output.xlsx')
        df.to_excel(writer, 'Sheet1')
        writer.save()
