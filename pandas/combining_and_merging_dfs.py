### Combining and Merging DataFrames ###

'''
In pandas, dataframes can be combined in a number of ways. The most used are:

pandas.merge    # connects rows in dfs based on one or more common keys. Similar to SQL JOINs
pandas.concat   # glues/stacks together objects along an axis
combine_first   # splices together overlapping data to fill in missing values in one obj with vals from the other

Below are some examples of each.

'''
import pandas as pd

## MERGING
# merge example
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
    'data1': range(7)})

df2 = DataFrame({'key': ['a', 'b', 'd'], 
    'data2': range(3)})

pd.merge(df1, df2, on='key')    # note: 'on=' specifies the column to perform the join on

# By default, this will be an INNER join - i.e. values not in both columns will be ommitted.
# Can also do LEFT, RIGHT, and OUT joins by passing these as parameters to 'how='.

# The column name that they are to be joined on does not need to be the same in both df's.
# Can specify the joining col for each by passing the col names to 'left_on=' and 'right_on', respectively.
# e.g.
df3 = DataFrame({'key1': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
    'data1': range(7)})

df4 = DataFrame({'key2': ['a', 'b', 'd'], 
    'data2': range(3)})

pd.merge(df1, df2, left_on='key1', right_on='key2')

# To merge using multiple keys, pass the column names as a list
pd.merge(left_df, right_df, on=['key1', 'key2'], how='outer')

# To handle overlapping column names (not used as keys), merge has a 'suffixes' parameter
# that will automatically add a suffix to col names that appear in both dfs but will
# end up as separate columns in the merged df. Therefore, the col names in the meged df
# will still be unique.
pd.merge(left_df, right_df, on='key1', suffixes=('_left', '_right'))
-> columns in resulting df : ['key1', 'key2_left', 'lval', 'key2_right', 'rval']    # for example!

# note: if there are overlapping col names and no 'suffixes' are passed, it will default to ('_x', '_y')


## CONCATENATING
# The pandas 'concat' method glues together Series or DataFrame objects.
# Here is a simple example using 3 Series with NO INDEX OVERLAP:
s1 = Series([0, 1], index=['a', 'b'])
s2 = Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = Series([5, 6], index=['f', 'g'])

pd.concat([s1, s2, s3])
->  a   0
    b   1
    c   2
    d   3
    e   4
    f   5
    g   6

# By defaul 'concat' operates along 'axis=0', producing another Series.
# If you passed 'axis=1' (i.e. along columns) you'd get:
->      0   1   2
    a   0   NaN NaN
    b   1   NaN NaN
    c   NaN 2   NaN
    d   NaN 3   NaN
    e   NaN 4   NaN
    f   NaN NaN 5
    g   NaN NaN 6

# You can see from the above that the defaul is an 'OUTER' join.
# To get an INNER join, pass 'inner' to the join= parameter.

# When concat'ing df's it might be useful to ignore the index if it is not useful in the context
# of the df (e.g. if it's just default numbers).
# In this case will want to pass 'ignore_index=True' to the concat() method.
pd.concat([df1, df2], ignore_index=True)


## COMBINE_FIRST
# Lastly, for objects with partially- or fully-overlapping indexes, can use 'combine_first()'
# to "fill in the gaps" where no value is present.
# For example:
df1 = DataFrame({'a': [1., np.nan, 5., np.nan],
                 'b': [np.nan, 2., np.nan, 6.],
                 'c': range(2, 18, 4)})

df2 = DataFrame({'a': [5., 4., np.nan, 3., 7.],
                 'b': [np.nan, 3., 4., 6., 8.]})

# note: df2 has more rows but fewer columns than df1!

df1.combine_first(df2)  # will take df1 and "fill in" any gaps using data from df2
->      a   b   c
    0   1   NaN 2
    1   4   2   6
    2   5   4   10
    3   3   6   14
    4   7   8   NaN

# notice that the 5th row was ADDED to df1 (exclusively from df2).



