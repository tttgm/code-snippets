### LINEAR AND LOGISTIC REGRESSION ###

# Import and necessary libraries like pandas, numpy, etc.


# Identify 'features' (i.e. input variables) and 'labels' (i.e. output variables)
# (note: features and labels must be numeric/numpy arrays)
# Split into 'training' and 'testing' sets.

x_train = input_training_variables
y_train = target_training_variables
x_test =  input_testing_variables
y_test = target_testing_variables


# LINEAR REGRESSION

# Import linear regression model
from sklearn.linear_model import LinearRegression

# Create linear regression object
lm = LinearRegression()

# Train the model using the training set
lm.fit(x_train, y_train)

# Check the score of the fit on UNSEEN data
lm.score(x_test, y_test)

# Predict output
pred = lm.predict(x_test)


# LOGISTIC REGRESSION

#Import ligistic regression model
from sklearn.linear_model import LogisticRegression

# Create logistic regression classifier object
lr = LogisticRegression()

# Train the model
lr.fit(x_train, y_train)

# Check the score
lr.score(x_test, y_test)

# Predict output
pred = lr.predict(x_tes)
