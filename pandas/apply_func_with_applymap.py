## Applying a function to a column in a dataframe ##

#Can use '.applymap()' to apply any function to each value in a DataFrame, generating a new dataframe of the modified values.

#Note that the function arguments ARE NOT INCLUDED in the call (not even the brackets!!)

'''
'.applymap()' is slightly different from '.apply()' in that '.apply()' will perform the action on each COLUMN in the array, 
where as '.applymap()' will modify each data point individually.
You can also use an 'axis' argument for .apply() so that you operate on each ROW (rather than each column).

.apply() can also be used to take a column (or row) and return a single value (e.g. the max). When this is used on an array, the output will therefore be a LINEAR SERIES.
'''