## USING THE CUT() FUNCTION TO MAKE 'BUCKETS' ##

#Use the cut() func to group data into buckets. For example, want to lump groups of years together in a new variable called 'year_joined.bucket' for dataframe 'pf':

df$year_joined.bucket <- cut(df$year_joined, breaks = c(2004, 2009, 2011, 2012, 2014))

'''
This will create the following groupings of data:
    (2004, 2009],
    (2009, 2011],
    (2011, 2012],
    (2012, 2014]    # note: '(' means exclusive, ']' means inclusive
'''