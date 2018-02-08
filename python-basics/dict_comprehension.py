### Dictionary comprehension ###

"""
	Can implement a 'dict comprehension' in a similar manner to list/set comprehensions wth the following syntax:

		{keyexpression: valueexpression for key, value in iterable}

		or

		{keyexpression: valueexpression for key, value in iterable if condition}

"""

# e.g. here's how we could create a dict where each key is the name of a file in the current
# directory and each value is the size of that file

file_sizes = {name: os.path.getsize(size) for name in os.listdir(".")}


# A dictionary comprehension is particularly useful for inverting all the keys/values in a dict
# i.e.
inverted_dict = {v: k for k, v in d.items()}
# note: this will fail unless the values are all unique (to be able to be used as keys)
