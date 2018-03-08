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

'''
For applying a function accross a Series (i.e. a single column of a DataFrame), use .map()
This is really handy to perform a modification on a columns values, or for transforming
only some of the data value (e.g. for tidying up certain strings) for which we can pass
a mapping dictionary.

See this stackoverflow page for a discussion of applymap() vs map() vs apply():
https://stackoverflow.com/questions/19798153/difference-between-map-applymap-and-apply-methods-in-pandas

'''

# e.g.
# In 'Python for Data Analysis', pg281: There is a 'Federal Electoral Commision' dataset
# that has been loaded as 'fec'.
# There is a column for tracking occupations of the entries in the dataset, called 'contrb_occupation'.
# However, there is inconsistent recording in this column: e.g. some say 'INFORMATION REQUESTED', while
# others will have 'INFORMATION REQUESTED PER BEST EFFOTS'.
# If we want to clean these up, we can use a mapping dict and the .map() method on the column.

# i.e.
occ_mapping = {
    'INFORMATION REQUESTED PER BEST EFFORTS': 'NOT PROVIDED',
    'INFORMATION REQUESTED': 'NOT PROVIDED',
    'INFORMATION REQUESTED (BEST EFFORTS)': 'NOT PROVIDED',
    'C.E.O.': 'CEO',
}

# Use the .get() method so that if the value is not in the dict, the value will be returned!
f = lambda x: occ_mapping.get(x, x)

# Now map the dict to replace the relevant entries in the column 'contrb_occupation'
fec.contrb_occupation = fec.contrb_occupation.map(f)

# Done!
