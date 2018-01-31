### Encoding categorical variables for for use in sklearn ###


'''
The sklearn library is extremely useful for predictive modeling with python. However,
it can only handle numerical data/variables/features.

Converting categorical variables to numerical ones is called 'encoding', and can be 
done using the 'preprocessing' package in sklearn.
'''

from sklearn.preprocessing import LabelEncoder

# Make list of variables you want to encode
categorical_variables = ['Sex', 'Gender', 'Town', 'Education']

# Create encoder object
le = LabelEncoder()

# Replace categorical variable entry with encoded value in a given dataframe 'df'
for i in categorical_variables:
    # Fit the encoder to each value/entry
    df[i] = le.fit_transform(df[i])

# Check by looking at the types of columns
df.dtypes