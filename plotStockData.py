import matplotlib.pyplot as plt
import seaborn; seaborn.set()
from runcontrol import controlparameters as cp


class plotStockData:

    def __init__(self,dataset):
        self.dataset = dataset


    def makeplot(self):

        self.dataset[cp['stockvaluetime']].plot()
        plt.title('Intraday Times Series for the MSFT stock (1 min)')
        plt.show()