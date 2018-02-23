### Timing code with %time and %timeit

'''
The IPython environment has two useful timing 'magic' functions baked in.

%time returns the time taken to run a given execution. Just place it before the statement/function, in the same line.

However, a single execution may vary slightly each time it's run - therefore, using %timeit will return
the average computational time over many runs. This is particularly useful for fast executions that you
want to optimize (prior to scale-up, for example)
'''

# e.g. time how long it takes to do a list comprehension
%time comp = [x for x in some_obj if x > 50]

# will output the cpu time required for the list comp
