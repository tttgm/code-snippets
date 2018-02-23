### Conditionals with np.where ###

# In NumPy we can achieve a much quicker, vectorized conditional flow by using the np.where()
# notation to replace if-else statements.

# For example
import numpy as np

arr = randn(4, 4)   # create a random number 4 X 4 array

# Replace all positive values with 2, and all negative values with -2. 
# The format is np.where(conditions, if, else)
# i.e.
np.where(arr > 0, 2, -2)
# note: that np usually does not copy arrays/collections, and so this will modify the ACTUAL arr

# Don't have to replace with a scalar value though, can pass an array, and the replacement will be from
# the same position as the element in the array passed
# i.e.
np.where(arr > 0, 2, arr)
# This will replace positive values with 2, and 'replace' negative values with their original value in the
# array (i.e., leave them unchanged).
