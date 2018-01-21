## Applying a function elementwise to a dataframe ##

#Can use '.applymap()' to apply any function to each value in a DataFrame, generating a new dataframe of the modified values.

#Note that the function arguments ARE NOT INCLUDED in the call (not even the brackets!!)
#For example:
df = pd.DataFrame(
    {'a': [0.3564, 0.8865, 0.3545, 0.9799],
    'b': [0.5252, 0.3123, 0.6546, 0.9345],
    'c': [0.7777, 0.4563, 0.4636, 0.3456]
    })
# creates a df with values that are all 4 decimal places.
# Can convert them all to 2 dp by using .applymap()
df = df.applymap(lambda x: '%.2f' % x)

'''
'.applymap()' is slightly different from '.apply()' in that '.apply()' will perform the action on each COLUMN in the array, 
where as '.applymap()' will modify each data point individually.
You can also use an 'axis' argument for .apply() so that you operate on each ROW (rather than each column).

.apply() can also be used to take a column (or row) and return a single value (e.g. the max). When this is used on an array, the output will therefore be a LINEAR SERIES.
'''