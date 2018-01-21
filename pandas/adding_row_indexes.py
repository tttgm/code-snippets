## Adding row indexes to Pandas dataframes ##
'''
Can add 'row names' by adding an 'index argument' when creating the array.
'''
#For example:
import pandas as pd

enrollments_df = pd.DataFram({
    'account_key': [448, 448, 448, 448, 448],
    'status': ['canceled', 'canceled', 'canceled', 'canceled', 'current'],
    'join_date': ['2014-11-10', '2014-11-05', '2015-01-27', '2014-11-10', '2015-11-12'],
    'days_to_cancel': [65, 5, 0, 0, np.nan],
    'is_udacity': [True, True, True, True, True]
}, index = [
    'Row 1', 'Row 2', 'Row 3', 'Row 4', 'Row 5'
])