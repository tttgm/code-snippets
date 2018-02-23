### Type casting in NumPy ###

'''
Can change the 'dtype' of values within a np array relatively easily with .astype()

Note: NumPy arrays require that all the values have the same type.

If a type can't be cast, a TypeError will be raised

'''

# examples
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr.dtype
-> dtype('int64')

float_arr = arr.astype(np.float64)

float_arr.dtype
-> dtype('float64')

# or strings to float

numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)     
# here the dtype is specified on creation via the 'dtype' parameter

numeric_strings.astype(float)   # note: numpy is smart enough to pick up what 'float' refers to (i.e. 'np.float64')
-> array([1.25, -9.6, 42.])


