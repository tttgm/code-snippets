## ACCESSING AND INDEXING DATA IN 2D PANDAS ARRAY ##

#To access the data you can use '.loc[]' and '.iloc[]'.

#To get an entire row by name:
enrollments_df.loc['Row 2']     # returns all elements of Row 2 as a list.

#or similarly by position:
enrollments_df.iloc[1]          # returns all elements of Row 2 (position row=1) as a list.

#To get a single element:
enrollments_df.iloc[1, 3]       # returns data at position row=1, col=3.

#or by name:
enrollments_df.loc['Row 4', 'status']   # returns point in row 'Row 4' and column 'status'.

#To access entire columns you don't need '.loc', just use indexing notation:
enrollments_df['join_date']     # returns values in the column 'join_date'