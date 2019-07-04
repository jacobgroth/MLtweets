import matplotlib.pyplot as plt
import seaborn; seaborn.set()
from runcontrol import controlparameters as cp


class plotStockData:

    def __init__(self,dataset,datatype):
        self.dataset = dataset
        self.datatype = datatype


    def makeplot(self):


        if self.datatype == 'STOCK':
            self.dataset[cp['stockvaluetime']].plot()
            plt.title('Intraday Times Series for the MSFT stock (1 min)')
            plt.show()

        elif self.datatype == 'FMT':
            self.dataset.plot()
            plt.title('EPS for top 100 companies on s&p500')
            plt.show()