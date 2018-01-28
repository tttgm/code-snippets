### The 'zip' function ###

# 'zip()' "pairs" up the elements of multiple lists, tuples, or other sequences and 
# returns a list of tuples!

seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']

zip(seq1, seq2)
>>> [('foo', 'one'), ('bar', 'two'), ('baz', 'three')]  # note: is a LIST of TUPLES

# Note that the number of elements (tuples) it produces is equal to the SHORTEST sequence passed in,
# the residual items in the other sequence(s) are just ommited.
# e.g.

seq1 = ['foo', 'bar', 'baz'] 
seq2 = [True, False]

zip(seq1, seq2)
>>> [('foo', True), ('bar', False)]     # only TWO tuples returned, as seq2 had only two elements

# Given a "zipped" sequence, zip() can actually be used cleverly to "unzip" the elements!
# e.g.
all_stars = [('Kevin', 'Durant'), ('James', 'Harden'), ('Jimmy', 'Butler')]

first_names, last_names = zip(*all_stars)

first_names
>>> ('Kevin', 'James', 'Jimmy')
last_names
>>> ('Durant', 'Harden', 'Butler')
