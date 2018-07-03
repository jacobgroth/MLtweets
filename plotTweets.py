import matplotlib.pyplot as plt
import seaborn; seaborn.set()
from runcontrol import controlparameters as cp


class plotTweets:

    def __init__(self,dataset):
        self.dataset = dataset


    def makeplot(self):

        print(self.dataset)
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.set_xlabel('date')
        ax1.set_ylabel('number of tweets')
        ax1.set_title("number of time a tweet contains the phase: {}".format(cp['searchphrase']))
        self.dataset.plot(style="o-")
        plt.legend(['data'], loc='upper left');

        plt.show()