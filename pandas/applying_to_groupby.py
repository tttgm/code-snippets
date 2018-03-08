### Applying func's element-wise to groupby objects ###

'''
Other than the normal aggregation functions (mean, sum, count, etc) you might want to pass
a specific, user-defined function.
This can be achieved by calling .apply(func) directly on the groupby object.

The function can really be anything, as long as it returns a scalar value or a pandas object.
These returned items will then be output in the frame containing the (hierarchical) grouped obj.

'''
# Note: will be using the tipping dataset 'tip' again...
# e.g. Define a function. Here, 'top()' returns the top 'n' items of a sorted df column.
def top(df, n=5, column='tip_pct'):
    return df.sort_values(by=column)[-n:]

# Now, create a groupby obj as desired, and pass the func directly to the .apply() method.
tips.groupby('smoker').apply(top)

# This will return the sorted 'top 5' lists for each sub-category in the groupby obj (in this
# case they're 'Yes' and 'No', referring to if a smoker or not).

# Note: function parameters can be passed directly in the .apply() method as well:
tips.groupby('smoker').apply(top, n=1, column='total_bill')     # this changes the returned list to a length of 1, and the column that si sorted is 'total_bill'

