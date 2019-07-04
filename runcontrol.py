controlparameters = {
    'pathToTwintModule': '/Users/rgjg/Dropbox/geekcode/andreas/twint',

    'outputCSVfile': '/home/jacob//Dropbox/geekcode/andreas/MLtweets/selectedtweets.csv',
    'legislatorsInfoDir': "/home/jacob/Dropbox/geekcode/andreas/congress-legislators/CSVfiles/",
    'companyInfoDir': "/home/jacob/Dropbox/geekcode/andreas/FMPdata/",


    # 'outputCSVfile': '/Users/rgjg/Dropbox/geekcode/andreas/MLtweets/selectedtweets.csv',
    # 'legislatorsInfoDir' : "/Users/rgjg/Dropbox/geekcode/andreas/congress-legislators/CSVfiles/",

    'username': [ 'dummy'],
    #'username': '',
    'startdate': '2017-10-10',
    'enddate': '2019-06-22',
    'maxtweets' : 100000000 ,
    #'searchphrases' : ['USA', 'fans'], # for more than one search phrase -> seperate by space
    'searchphrases' : ['Wall Street', 'economics', 'recession' ], # for more than one search phrase -> seperate by space
    'twitterOutputdata': 'twitterdata',
    'stockindex' : "^GSPC",  # s&p500 use  "^IXIC" for nasdaq
    'stockvaluetime' : 'Close' # Use for instance "Open" for opening stock value

}