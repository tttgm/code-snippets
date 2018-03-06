### RESHAPING AND PIVOTING IN PANDAS ###

## STACK/UNSTACK DATA
# Hierarchical indexing gives a consistent way to rearrange data in a df.
# The two most used methods are:
df.stack()  # this "rotates" or pivots columns --> rows
df.unstack()    # this pivots rows --> columns

# Can think of it like 'stack()' is "stacking" the columns on top of each other (i.e., into rows),
# whereas 'unstack()' is doing the opposite.

# By default, the INNER MOST level in the hierarchy is the one that is stacked/unstacked, but you
# can specify this explicitly by passing the 'name' to the method.
# e.g.
data = DataFrame(np.arange(6).reshape((2, 3)),
                 index=pd.Index(['Ohio', 'Colorado'], name='state'),
                 columns=pd.Index(['one', 'two', 'three'], name='number'))

data
->  number      one     two     three
    state
    Ohio        0       1       2
    Colorado    3       4       5


stacked_data = data.stack()
->  state       number
    Ohio        one         0
                two         1
                three       2
    Colorado    one         3
                two         4
                three       5

# Remember that the default is the inner-most level that gets stacked/unstacked, but can override that
# by passing the 'name'.
# e.g.
unstacked_data = stacked_data.unstack('stack')
->  state   Ohio    Colorado
    number  
    one     0       3
    two     1       4
    three   2       5

## PIVOTING FROM "LONG" TO "WIDE" FORMAT
# Timeseries data is typically stored in so-called "long" or "stacked" format (i.e. lots of rows!)
# For investigating this kind of data in a DataFrame it might be easier to separate out into
# more columns.
# This is what the 'pivot()' method does.
df.pivot('row_index', 'col_index', 'values')    # these parameters are the COLUMN names to be used as these functions

# When the last of these 3 parameters is ommited (i.e. 'values'), a df with hierarchical columns
# is returned.

# NOTE: when operating like this (ommiting the 3rd parameter), .pivot() is really just a shortcut
# for creating a hierarchical index using 'set_index' and reshaping with .unstack()
# i.e.
df.set_index(['row_index', 'col_index']).unstack('values')
# will produce the same output as:
df.pivot('row_index', 'col_index')

