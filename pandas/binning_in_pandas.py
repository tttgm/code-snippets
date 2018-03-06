### Binning in pandas ###

# You can perform 'discretization' and binning in pandas easily with the .cut() (and .qcut()) methods.

# For example, imagine you want to bin together a list of ages into 'age brackets'
ages = [19, 62, 32, 23, 53, 35, 69, 20, 28]

# Set the cut-off ages for the bins by creating a list with the upper & lower limits:
bins = [18, 25, 35, 60, 100]
# i.e. this will create bins of 18-25, 26-35, 36-60, and 61-100.

# The pandas lib has .cut() built-in
import pandas as pd 

binned_ages = pd.cut(ages, bins)    # the params are 'list of values/data' and the 'bin limits'

# 'binned_ages' is now a 'Categorical' pandas obj with info on where each value in 'ages' is binned.
# This obj has 'labels' and 'levels' attributes built-in that can be called on it:
binned_ages.labels
-> array([0, 3, 1, 0, 2, 1, 3, 0, 2])   # i.e. a 'label' (index) assigned to each bin

binned_ages.levels
-> array([(18, 25], (25, 35], (35, 60], (60, 100]])     # note: '(' means EXCLUSIVE, ']' means INCLUSIVE

# Can change which side of the 'level' is inclusive by passing 'right=False' to the .cut() method.

#.qcut() just divides the data into equal-sized bins - i.e., do not pre-define the 'ranges'

