### Deleting rows or columns of a pandas dataframe ###


# Although you can use the 'del' keyword - e.g.
del df['column_name']

# it is considered better practice to use 'drop', and specify whether it is a column or row
# to be removed using the 'axis' parameter.
# (note: axis = 0 for rows and 1 for columns)
# e.g.
df = df.drop('column_name', axis=1)

# or remove a row via it's index
# e.g.
df = df.drop('row_index', axis=0)
