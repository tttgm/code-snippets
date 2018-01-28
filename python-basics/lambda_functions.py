### Lambda (or 'anonymous') functions ###

# "Lambda functions" are really just simple functions consisting of a single statement, the result
# of which is the return value.
# They are defined using the 'lambda' keyword.

# e.g., the following two functions are equivalent
def short_function(x):
    return x * 2

# and

equiv_lambda = lambda x: x * 2

# They are particularly useful for data analysis, as there are many times where data transformation functions
# will take FUNCTIONS as arguments.

# note: one of the reasons lambda functions are sometimes called "anonymous functions" is because the function
# obj itself is never given a name attribute!

