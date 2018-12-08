class tweet:

    """ A generic class to hold relevant data for a plot """

    def __init__(self):
        self.username = ''
        self.text = ''
        self.date = ''
        self.retweets = 0


    def __init__(self, username = '' , text = '', date = '', retweets = 0):

        self.username = username
        self.text = text
        self.date = date
        self.retweets = retweets