### Multiple aggregation functions or column-dependent funcs ###

'''
You can return multiple aggregation function outputs (e.g. mean, sum, count, max) by passing them as a
LIST to the .agg() method (called on a groupby object).

Renaming the resulting frame columns is easy - just pass the functions to the .agg() method as a tuple,
with the first item in the tuple the NAME, and the second item the FUNC.

If you want to apply DIFFERENT functions to different groups/data, pass a DICT to the .agg() method
that maps the column names to the specific func you want to call on it.

'''

# e.g.
# note: Using data taken from a dataset of tipping in America
grouped = tips.groupby(['sex', 'smoker'])   # groups the 'tips' df by these two categories

grouped_pct = grouped['tip_pct']    # 'tip_pct' is a column in the df containing the tip %
grouped_pct.agg('mean')
->                     
    sex     smoker
    Female  No      0.1569 
            Yes     0.1822
    Male    No      0.1607
            Yes     0.1528
# this has returned the mean values in the hierarchical sex/smoker groupby obj


# Can pass MULTIPLE functions as a LIST
grouped_pct.agg(['mean', 'std', np.max])
->                  mean    std     np.max           
    sex     smoker
    Female  No      0.1569  0.0364  0.1959 
            Yes     0.1822  0.0716  0.3602
    Male    No      0.1607  0.0418  0.2202
            Yes     0.1528  0.0906  0.6747

# To RENAME the output, pass list of TUPLES
grouped_pct.agg([('Average', 'mean'), ('Standard Dev', 'std'), ('Maximum', 'max')])
->                  Average    Standard Dev     Maximum           
    sex     smoker
    Female  No      0.1569     0.0364           0.1959 
            Yes     0.1822     0.0716           0.3602
    Male    No      0.1607     0.0418           0.2202
            Yes     0.1528     0.0906           0.6747


# To MAP the desired function onto specific columns, pass a DICT
grouped.agg({'tip': np.max, 'size': 'sum'})
# This returns a frame with the 'max' for the 'tip' column (as grouped by 'sex' and 'smoker') and
# the 'sum' of the 'size' column.
# Of course, can return multiple values for each of these columns by passing a LIST as the val in the
# above dict!


### SPECIAL NOTE:
# As most of the above transformation return indexed (often hierarchical) dataframes, you can instead
# return more of a 'flat' dataframe by passing 'as_index=False' to the .groupby() method.

