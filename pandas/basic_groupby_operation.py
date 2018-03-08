### Basic groupby() operation ###

'''
The pandas .groupby() method provides a powerful and versatile way of aggregating data in Series or 
DataFrame objects.

Think of the procedure according to the 'Spilt-Apply-Combine' principle. The data is first split
into groups, then an aggregation function (e.g. mean, sum, stddev, etc) is applied to each group,
the data is then combined back into a dataframe to yield the output.

'''
# e.g.
from pandas import DataFrame

df = DataFrame({'Team': ['TOR', 'DEN', 'WAS', 'BOS', 'DEN', 'DEN', 'WAS'],
                'Player': ['Lowry', 'Jokic', 'Beal', 'Irving', 'Murray', 'Harris', 'Wall'],
               'o_rating': np.random.randint(10, size=7),
               'd_rating': np.random.randint(10, size=7)})
df
->  x   Player  Team    d_rating    o_rating
    0   Lowry   TOR     4           3
    1   Jokic   DEN     0           0
    2   Beal    WAS     6           7
    3   Irving  BOS     3           2
    4   Murray  DEN     8           9
    5   Harris  DEN     9           4
    6   Wall    WAS     3           9

# Create 'groupby object', with the desired value to be measured 'o_rating' grouped by 'Team'
grouped = df['o_rating'].groupby(df['Team'])
grouped.mean()
->  Team
    BOS     2.00
    DEN     4.33
    TOR     3.00
    WAS     8.00

# Can groupby more than one category -- results in a hierarchically-structured output.
# Do the groupby on multiple cat's by passing them as a LIST.
# i.e.
grouped = df['d_rating'].groupby([df['Team'], df['Player']])
grouped.sum()
->  Team    Player
    BOS     Irving      3
    DEN     Harris      9
            Jokic       0
            Murray      8
    TOR     Lowry       4
    WAS     Beal        6
            Wall        3

# Note: the output values above refer to the 'd_rating' data

# Can use .unstack() to transform the 'long' hierarchical data into a 'wide' format dataframe!


