import matplotlib.pyplot as plt
import seaborn; seaborn.set()
from runcontrol import controlparameters as cp


class plotCombined:

    def __init__(self,dataset):
        self.dataset = dataset


    def makeplot(self):

        fig = plt.figure()

        fig, ax1 = plt.subplots()

        #ax1.plot(t, s1, 'b-')
        self.dataset['negative tweets'].plot(style="bo-", label='negative tweets')
        self.dataset['positive tweets'].plot(style="b--", label='positive tweets')
        # Make the y-axis label, ticks and tick labels match the line color.
        ax1.set_ylabel('Number of tweets (#)', color='b')
        ax1.tick_params('y', colors='b')

        #plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1,
        #           ncol=1, mode="expand", borderaxespad=0.)
        plt.legend(loc='upper left')

        ax2 = ax1.twinx()

        self.dataset['FMPdata'].plot(style="ro-", label='Free Cash Flow')
        ax2.set_ylabel('Free Cash Flow ($)', color='r')
        ax2.tick_params('y', colors='r')
        ax2.set_xlabel('Date')
        ax2.set_title("Free Cash flow and number of time a tweet contains the phase: {} ".format(cp['searchphrases']))

        plt.legend()



        fig.tight_layout()


        plt.show()