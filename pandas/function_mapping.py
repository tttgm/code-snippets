### Applying functions to elements in a dataframe ###

'''
Many functions can be applied elementwise (vectorized) to pandas df's automatically as for NumPy arrays,
but if you want you can write custom functions that get applied either in 1D (i.e. across an
array), using .apply(), or across the entire matrix using .applymap().

'''

# For example, using this dataframe:
from pandas import DataFrame

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

df = DataFrame(arr, columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])

df
->          b   d   e 
    Utah    1   2   3
    Ohio    4   5   6
    Texas   7   8   9
    Oregon  10  11  12

# Appling a function across 1D
# e.g.
f = lamba x: x.max() + x.min()      # some arbitrary function

df.apply(f)     # axis default is 0 (i.e. down each COLUMN)
->  b   11
    d   13
    e   15

df.apply(f, axis=1)     # axis=1 means perform func across each ROW
->  Utah    4
    Ohio    10
    Texas   16
    Oregon  22


# Can apply elementwise across all elements in df
# e.g.
g = lambda x: '%.1f' % x     # convert value to float and report to 1 d.p.

df.applymap(g)
->          b       d       e 
    Utah    1.0     2.0     3.0
    Ohio    4.0     5.0     6.0
    Texas   7.0     8.0     9.0
    Oregon  10.0    11.0    12.0

