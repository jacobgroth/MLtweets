import matplotlib.pyplot as plt
import seaborn; seaborn.set()
from runcontrol import controlparameters as cp


class plotTweets:

    def __init__(self,dataset):
        self.dataset = dataset


    def makeplot(self):

        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.set_xlabel('date')
        ax1.set_ylabel('number of tweets and stock rate')
        ax1.set_title("number of time a tweet contains the phase: {} and MSFT stock rate".format(cp['searchphrases']))

        for key, value in self.dataset.items():
            value.plot(style="o-",label=key)

        plt.legend()

        plt.show()