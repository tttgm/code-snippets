### Handling Missing Data in Pandas ###

# 'NaN' is the representation of missing data in pandas, and it responds to np's .isnull() call.

# Some common missing data methods:
.dropna()   # filter axis labels based on whether values for each label have missing data - is tunable
.fillna()   # fill missing data with some value (or use interpolation such as 'ffill' or 'bfill')
.isnull()   # return like-type obj containing boolean values indicating presence of NaN
.notnull()  # negation of '.isnull()'


## DROPPING ROWS/COLS BASED ON MISSING DATA

# Example of how .dropna() works for df's
# By default, it will drop rows in which ANY NaN appears:
df = DataFrame([[1., 6.5, 3.], [1., NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])

df
->      0   1   2
    0   1   6.5 3
    1   1   NaN NaN
    2   NaN NaN NaN
    3   NaN 6.5 3

df.dropna()
->      0   1   2
    0   1   6.5 3

# Can only drop rows for which ALL of the values are NaN by passing how='all'
df.dropna(how='all')
->      0   1   2
    0   1   6.5 3
    1   1   NaN NaN
    3   NaN 6.5 3

# Can drop columns in the same way by passing 'axis=1'
df.dropna(axis=1, how='all')
# in this case wouldn't drop anything as all columns contain at least one actual value!

# Alteratively, you can use the 'thresh=' parameter to say how many (non-NaN) values a row/col must have to be kept.
# e.g.
df.dropna(thresh=2)
->      0   1   2
    0   1   6.5 3
    3   NaN 6.5 3

## FILLING IN MISSING DATA WITH SOME VALUES

# For this, will mostly use .fillna()
# e.g.
df.fillna(0)
->      0   1   2
    0   1   6.5 3
    1   1   0   0
    2   0   0   0
    3   0   6.5 3

# Passing a dict, you can specify a different value for each column
# e.g.
df.fillna({1: 0.5, 2: -0.5})
df
->      0   1   2
    0   1   6.5 3
    1   1   0.5 -0.5
    2   NaN 0.5 -0.5
    3   NaN 6.5 3

# Or can use .mean(), or 'ffill' (forward fill - fill with previous value)

# Here are the .fillna() arguments:
value   # scalar value or dict-like obj to fill missing values
method  # interpolation, by default 'ffill' if function called with no arguments
axis    # axis to fill on (default axis=0)
inplace # set to 'True' if you want to modify the obj without producing a copy
limit   # for forward/backward filling, the max no. of consecutive periods to fill


### Finding the number of empty entries in a dataframe ###

# This will look for 'isnull()' entries down each column (i.e. 'axis=0') and return the count ('sum()')
df.apply(lambda x: sum(x.isnull()), axis=0)

# The most simple way to replace these empty entries may be to replace them with the mean() of that col
df['col_name'].fillna(df['col_name'].mean(), inplace=True)
