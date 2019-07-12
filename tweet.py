class tweet:

    """ A generic class to hold relevant data for a plot """

    def __init__(self):
        self.username = ''
        self.text = ''
        self.date = ''
        self.retweets = 0
        self.bioguide = ''
        self.type = ''
        self.state = ''
        self.party = ''



    def __init__(self, username = '' , text = '', date = '', retweets = 0, bioguide = '', legtype = '', state = '', party = '' ):

        self.username = username
        self.text = text
        self.date = date
        self.retweets = retweets
        self.bioguide = bioguide
        self.legtype = legtype
        self.state = state
        self.party = party
