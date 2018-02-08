### Recursive functions ###

# "Recursive functions" are functions that call themselves from within the function body.
# They can be seen as having two cases: the "base case" and the "recursive case"

# A classic example of a recursive function is in the calculation of factorials.
# e.g. 5! (that is, 5 x 4 x 3 x 2 x 1) is:
def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x - 1)

# In this algorithm, if the number x is 1 or less, 1 is returned and no recursion occurs -- this is the "base case".
# If x is greater than 1, then the second return statement gets called, including the factorial() function
# itself -- this is the "recursive case".

# You need to be careful not to setup an infinite recursion; but in the above example the function will always
# terminate once x becomes 1.

