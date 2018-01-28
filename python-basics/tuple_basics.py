### Tuples ###

# A tuple is a one-dimensional, fixed-length, IMMUTABLE sequence of Python onjects.
# The easiest way to create one is with a comma-separated sequence of values:

tup = 4, 2, 6

print tup
>>> (4, 2, 6)

# Any iterable can be converted to a tuple using the tuple() method
tuple([4, 5, 6])    # convert a list into a tuple
print tup
>>> (4, 5, 6)

# 'Unpacking' tuples
tup = (4, 5, 6)
a, b, c = tup   # unpack using simple assignment, where each of the letters (a, b, c) are assigned to the corresponding sequence of values in the tuple
print b
>>> 5

# A useful instance method for tuples (and also lists) is 'count()', which counts the number of occurances
a = (1, 2, 2, 5, 3, 2, 4, 2)
a.count(2)
>>> 4

