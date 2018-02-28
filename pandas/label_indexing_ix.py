### Label-Indexing with special indexing field 'ix' in pandas ###

'''
There are a number of ways to slice or filter a pandas dataframe. Much of the high-level operation
is wrapped up in the 'ix' indexing function.

'''

# Some dataframe indexing options

df[val]     # select a single col or sequence of columns. Special case conviences: boolean arra (filter rows
# slice (slice rows), or boolean dataframe (set values based on criterion))

df.ix[val]  # selects single row of subset of rows from the df
df.ix[:, val]   # selects single column from subset of columns
df.ix[val1, val2]   # select both rows and columns!

