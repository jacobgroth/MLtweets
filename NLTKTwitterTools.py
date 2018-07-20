import string
import re

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer
from random import shuffle

from nltk import classify
from nltk import NaiveBayesClassifier


class NLTKTwitterToolsClass:

    # this class build largely on the examples presented on the website here : http://blog.chapagain.com.np/python-nltk-twitter-sentiment-analysis-natural-language-processing-nlp/


    def __init__(self):

        self.stopwords_english = stopwords.words('english')
        self.stemmer = PorterStemmer()

        # Happy Emoticons
        emoticons_happy = set([
            ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
            ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
            '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
            'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
            '<3'
        ])

        # Sad Emoticons
        emoticons_sad = set([
            ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
            ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
            ':c', ':{', '>:\\', ';('
        ])

        # all emoticons (happy + sad)
        self.emoticons = emoticons_happy.union(emoticons_sad)

    def cleanTweet(self,tweet):
        # remove stock market tickers like $GE
        tweet = re.sub(r'\$\w*', '', tweet)

        # remove old style retweet text "RT"
        tweet = re.sub(r'^RT[\s]+', '', tweet)

        # remove hyperlinks
        tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)

        # remove hashtags
        # only removing the hash # sign from the word
        tweet = re.sub(r'#', '', tweet)

        # tokenize tweets
        tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
        tweet_tokens = tokenizer.tokenize(tweet)

        tweet_clean = []
        for word in tweet_tokens:
            if (word not in self.stopwords_english and # remove stopwords
                  word not in self.emoticons and # remove emoticons
                    word not in string.punctuation): # remove punctuation
                #tweets_clean.append(word)
                stem_word = self.stemmer.stem(word) # stemming word
                tweet_clean.append(stem_word)

        return tweet_clean


    def cleanTweets(self,tweets):

        cleanTweetsReturn = []
        for tweet in tweets:
            tweet.txt =  " ".join(self.cleanTweet(tweet.text))
            cleanTweetsReturn.append(tweet)

        return cleanTweetsReturn


    # feature extractor function
    def bag_of_words(self,tweet):
        words = self.cleanTweet(tweet)
        words_dictionary = dict([word, True] for word in words)
        return words_dictionary


    def trainNaiveBayesClassifier(self):

        from nltk.corpus import twitter_samples


        pos_tweets = twitter_samples.strings('positive_tweets.json')
        neg_tweets = twitter_samples.strings('negative_tweets.json')

        # positive tweets feature set
        pos_tweets_set = []
        for tweet in pos_tweets:
            pos_tweets_set.append((self.bag_of_words(tweet), 'pos'))

        # negative tweets feature set
        neg_tweets_set = []
        for tweet in neg_tweets:
            neg_tweets_set.append((self.bag_of_words(tweet), 'neg'))


        # radomize pos_reviews_set and neg_reviews_set
        # doing so will output different accuracy result everytime we run the program
        shuffle(pos_tweets_set)
        shuffle(neg_tweets_set)

        test_set = pos_tweets_set[:1000] + neg_tweets_set[:1000]
        train_set = pos_tweets_set[1000:] + neg_tweets_set[1000:]


        self.classifier = NaiveBayesClassifier.train(train_set)



    def classifyTweets(self,tweets):

        returntweets = []
        for tweet in tweets:
            custom_tweet_set = self.bag_of_words(tweet.text)
            tweet.sentiment = self.classifier.classify(custom_tweet_set)
            returntweets.append(tweet)

        return returntweets

    def splitIntoPosAndNeg(self,tweets):

        posTweets = []
        negTweets = []
        for tweet in tweets:

            if tweet.sentiment == 'pos':
                posTweets.append(tweet)

            else:
                negTweets.append(tweet)

        return posTweets, negTweets


