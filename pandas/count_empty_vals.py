### Finding the number of empty entries in a dataframe ###

# This will look for 'isnull()' entries down each column (i.e. 'axis=0') and return the count ('sum()')
df.apply(lambda x: sum(x.isnull()), axis=0)