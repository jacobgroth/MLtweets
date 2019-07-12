from runcontrol import controlparameters as cp

import pandas as pd

class getLegislatorInfoClass:

    def __init__(self):
        self.socialmediaCSV = cp['legislatorsInfoDir'] + 'legislators-socialemedia.csv'
        self.legislatorsCSV = cp['legislatorsInfoDir'] + 'legislators-current.csv'
        self.historicalCSV = cp['legislatorsInfoDir'] + 'legislators-historical.csv'


    def getInfo(self):
        socialmedia_df = pd.read_csv(self.socialmediaCSV)
        legislators_df = pd.read_csv(self.legislatorsCSV)
        historical_df = pd.read_csv(self.historicalCSV)

        merged_outer_historical = pd.merge(left=socialmedia_df,right=historical_df,how='outer',left_on='id__bioguide',right_on='bioguide_id')
        merged_outer = pd.merge(left=socialmedia_df,right=legislators_df,how='outer',left_on='id__bioguide',right_on='bioguide_id')

        #print(merged_outer.columns)

        filtered_merged_historical = merged_outer_historical[merged_outer_historical['social__twitter'].notnull()]
        filtered_merged_outer = merged_outer[merged_outer['social__twitter'].notnull()]

        final_df = filtered_merged_outer.filter(['id__bioguide','social__twitter','type', 'state','party'])

        return final_df