### Iterable striding ###

"""
	Can access every 'other' entry of a list or string (or other iterable) via 'striding'.
"""
# e.g.

mvps = ['D-Rose', 'LeBron', 'Steph', 'KD', 'Russ', 'Giannis']

# access every second entry
print mvps[::2]
# >>> ['D-Rose', 'Steph', 'Russ']

# start from index 1 and take every second item
print mvps[1::2]
# >>> ['LeBron', 'KD', 'Giannis']

# can perform manipulations on stride slices
mvps[1::2] = ['Harden'] * len(mvps[1::2])
print mvps
# >>> ['D-Rose', 'Harden', 'Steph', 'Harden', 'Russ', 'Harden']

