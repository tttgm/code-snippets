### Create Dummy Variables in Pandas ###

'''
'Dummy' variables are commonly used for statistical modeling and machine learning applications.
These are essentially just a boolean list of wheather a certain feature exists in a row or not.

These can (relatively) easily be created in pandas using the .get_dummies() method.
'''

# e.g.
import pandas as pd 

df = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                'data1': range(6)})

# Call .get_dummies() on dataframe and pass column you want to convert to dummy variables
dummies = pd.get_dummies(df['key'])

dummies
->      a   b   c 
    0   0   1   0
    1   0   1   0
    2   1   0   0
    3   0   0   1
    4   1   0   0
    5   0   1   0

# Can re-name the dummy var col's using the 'prefix=' parameter in the .get_dummies() method.
# i.e.
dummies = pd.get_dummies(df['key'], prefix='key')

# Will also re-attach the dummy var's created to the original df.
df_with_dummies = df[['data1']].join(dummies)   # note: only included the 'data1' col of the original df

df_with_dummies
->      data1   key_a   key_b   key_c 
    0   0       0       1       0
    1   1       0       1       0
    2   2       1       0       0
    3   3       0       0       1
    4   4       1       0       0
    5   5       0       1       0

