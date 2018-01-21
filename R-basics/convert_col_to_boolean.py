## Converting columns to Boolean/logical values ##
'''
If some columns contain a lot of zeros, because for example the user hasn't used that feature, 
you may not want these values affecting the statistics.
To avoid this you can create a new 'logical' column that says whether the value in the other column is non-zero or not.
'''

#Can write 'if-else' statements in R simply using the following syntax:

ifelse(logical_check, if-assignment, else-assignment)
# this performs the logic statement 'logical check' -> if TRUE, the value assigned is 'if-assignment', if FALSE the value assigned is 'else-assignment'

#Can easily create a new column for these values by:
df$column_name <- ifelse(something, val1, val2)     # create column named 'column_name' and fill with logic

#e.g.
df$mobile_check_in <- ifelse(df$mobile_likes > 0, 1, 0)
