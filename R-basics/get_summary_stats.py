## GETTING SUMMARY STATISTICS ##

#Can use the table() command to get summary stats easily presented.

#e.g.
table(df$variable)  # returns a simple 'count' of grouped values in the column named 'variable'

'''
For a more detailed overview, use the 'by()' command.
This takes 3 parameters: a variable, a categorical variable, and a function.
'''

#e.g.
by(df$friend_count, df$gender, summary)     # 'summary' is standard function that returns basic stats

