### Finding the number of empty entries in a dataframe ###

# This will look for 'isnull()' entries down each column (i.e. 'axis=0') and return the count ('sum()')
df.apply(lambda x: sum(x.isnull()), axis=0)

# The most simple way to replace these empty entries may be to replace them with the mean() of that col
df['col_name'].fillna(df['col_name'].mean(), inplace=True)

