### Starred expressions ###

"""
	In some situations we want to take two or more pieces of a list or tuple in one go.
	We can do this using sequence unpacking. The * operator can be used to grab whatever is left
	over after taking iterables piecewise.

	This might be particularly useful for slicing strings (e.g. URLs) and just keeping/storing certain parts.
"""

# e.g.

first, *rest = [9, 2, -4, 8, 7]

print first, rest

# >>> 9, [2, -4, 8, 7]

# or

first, *mid, last = "Charles Philip Arthur George Windsor".split()

print first, mid, last

# >>> 'Charles', ['Philip', 'Arthur', 'George'], 'Windsor'
