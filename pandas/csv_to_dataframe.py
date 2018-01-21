# IMPORTING CSV TO DATAFRAMES ##

#DataFrames are particularly suited to reading and interpreting .csv files.

#Pandas has a function expecially for this, called '.read_csv()':

import pandas as pd

pd.read_csv('file_name.csv')        # loads data from .csv file directly into a Pandas DataFrame

'''
Note: to access by row or by col you can use the axis=1 or axis=0 arguments, but you can also just use axis='index' (for rows) and axis='columns' (for col).
HOWEVER, this is actually a bit misleading, as using axis='columns' will not give (e.g.) the mean of each column, but will actually give the mean of each row!!
The idea here is that you are taking the mean 'along each column' (for a give row)...
'''