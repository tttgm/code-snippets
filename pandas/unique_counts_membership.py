### Unique Values, Value Counts, and Membership ###

# The unique values contained in a pandas Series can be found by calling .unique()

obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])

obj.unique()
-> ['c', 'a', 'd', 'b']

# Similarly, .value_counts() returns a frequency table with value counts.
# e.g.
obj.value_counts()
->  c   3 
    a   3 
    b   2 
    d   1

# Membership testing in pandas can be done using .isin(), and can be done on both Series and df's.
# This returns a corresponding Boolean array.
# e.g.
obj.isin(['b', 'c']) # testing the values in 'obj' to see if they are in the list passed to .isin (i.e. ['b', 'c'])
->  0   True
    1   False   
    2   False    
    3   False
    4   False
    5   True
    6   True

