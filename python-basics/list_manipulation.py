### List manipulation ###

"""
	There are a number of convenient functions to manipulate lists.
	Some are shown below.
"""

mvps = ['D-Rose', 'LeBron', 'Steph', 'KD', 'Russ']


# can add to the end of the list with .append()
mvps.append('Giannis')
print mvps
# >>> ['D-Rose', 'LeBron', 'Steph', 'KD', 'Russ', 'Giannis']

# can remove the right-most entry with .pop()
mvps.pop()
print mvps
# >>> ['D-Rose', 'LeBron', 'Steph', 'KD', 'Russ']

# can insert at a given index using either
mvps[1:1] = ['Kobe']
# or
mvps.insert(1, 'Kobe') 	# insert 'Kobe' at index 1
print mvps
# >>> ['D-Rose', 'Kobe', 'LeBron', 'Steph', 'KD', 'Russ']

# can also remove slices two ways, like
mvps[1:3] = [] 	# assign this slice to an empty string
# or
del mvps[1:3]
print mvps
# >>> ['D-Rose', 'Steph', 'KD', 'Russ']


