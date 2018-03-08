### Indexing and selecting groupby() objects ###

'''
Especially for large datasets, we often want the groupby to return certain columns.
We can use indexing/slicing to acheive this.

'''

# Firstly, note that by selecting a column by the usual df selection method is equivalent to calling
# the groupby on that column.
# i.e.

df.groupby('Player')['score']
df.groupby('Player')['rating']

# are equivalent to

df['score'].groupby(df['Player'])
df['rating'].groupby(df['Player'])


# Therefore, to select only the desired columns from the dataframe to be included in the grouped
# object, just pass them as a LIST to following the grouping method.
# e.g.
df.groupby('Team')[['score', 'rating']]

# note: in the example above, the data/values 'score' and 'rating' are contated WITHIN a LIST in the 
# column(s) selection!
