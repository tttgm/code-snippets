### Sorting and Ordering DataFrames and Series in Pandas ###

# To order a Series by its values, use the .order() method.
# Missing values (i.e. NaN) are sorted to the end/bottom by default.

# e.g.
obj = Series([4, 7, -3, 2])

obj.order()
-> [-3, 2, 4, 7]

# To sort a column in a dataframe use the .sort_index() method with the 'by=col_name' parameter
# e.g.
df = DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})

df
->  a   b
    0   4   
    1   7   
    0   -3  
    1   2

df.sort_index(by='b')
->  a   b   
    0   -3  
    1   2 
    0   4 
    1   7

# To sort by multiple columns, pass them as a list to the 'by=' parameter.
# Note that the sorting order will preferentially by the order they are passed to 'by='
# e.g.
df.sort_index(by=['a', 'b'])
->  a   b
    0   -3 
    0   4 
    1   2 
    1   7


