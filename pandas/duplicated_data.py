### Duplicated Data ###

'''
In pandas, the method .duplicated() will identify any ROWS that are duplicates. Calling this method on a
dataframe will return a Boolean list indicating which entries are duplicates.

Relatedly, .drop_duplicates() will return a dataframe with any duplicated rows removed.

Note: By default, these both check ALL COLUMNS to identify duplicates. To check an individual column
(or columns) for duplicates, just pass the col name as a list.
'''

# e.g.
data = DataFrame({'tom': ['cool'] x 3 + ['rad'] X 3,
                    'count' = [1, 1, 3, 5, 6, 5]})

data
->      tom     count
    0   cool    1
    1   cool    1
    2   cool    3
    3   rad     5
    4   rad     6
    5   rad     5

# Check for duplicated ROWS with .duplicated()
data.duplicated()
->  0   False
    1   True
    2   False
    3   False
    4   False
    5   True

# Notice that the FIRST row will be kept (i.e. NOT identified as a duplicate)

# Can just remove duplicates in a single column(s) by passing it as a list
data.drop_duplicates(['tom'])
->      tom     count
    0   cool    1
    3   rad     5
