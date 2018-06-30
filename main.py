from helperClasses import *


tweets = getTweets()

selectedTweets = tweets.GetTheLast10TopTweetsByUsername(10)

for tweet in selectedTweets:

    if "Bush" in tweet.text:
        print(tweet.text, tweet.date)