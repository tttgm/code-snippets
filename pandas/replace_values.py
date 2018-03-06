### Replacing Values in a DataFrame or Series ###

# We can use the .replace(old_val, new_val) method to quickly replace certain values in a pandas data obj.

# e.g.
# Consider we have some df, where -999 is used in the imported dataset to replresent a missing value.
# We can easily replace that with NaN via the following:
df.replace(-999. np.nan)    # use the numpy NaN feature

# If you want to replace multiple values, just pass them as a list.
# i.e.
df.replace([-999, 0.0, -1000], np.nan)  # replaces them all with NaN

# Or, can 'map' replacement values using a dictionary.
# i.e.
df.replace({-999: np.nan, 0.0: 'nothing', -1000: -10})

