### List, Set, and Dict Comprehensions ###

# List comprehensions allow you to easily form a new list by filtering the elements of a collection and transforming
# the elements passing the filter in one concise expression.
# e.g.
new_list = [expression for value in collection if condition]

# This is equivalent to the following loop:
new_list = []
for value in collection:
    if condition:
        new_list.append(expression)

# The filter condition can also be ommited, leaving only the expression.

# Set and Dict comprehensions are a natural extension of this.
# The syntax for a "dict comprehension" is as follows:
dict_comp = {key-expression : value-expression for value in collection if condition}

# and for a "set comprehension":
set_comp = {expression for value in collection if condition}

# Here is an example of a dict comprehension (the list and set versions are relatively simple):
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']

# this dict will map the location of the entries in the 'string' list with thier values
loc_mapping = {val : index for index, val in enumerate(strings)}    # note the use of enumerate()

loc_mapping
>>> {'a': 0, 'as': 1, 'bat': 2, 'car': 3, 'dove': 4, 'python': 5}

# You can nest multiple list comprehensions, although they become a bit difficult to understand...
# i.e.
new_list = [expression for value in collection for expression in value if condition]

# an example:
# Get all of the names from this list-of-list's that have 2 or more e's in them
all_data = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'], 
            ['Suzie', 'Casey', 'Jill', 'Ana', 'Eva', 'Jennifer', 'Stephanie']]

result = [name for names in all_data for name in names if name.count('e') >= 2]
result
>>> ['Jefferson', 'Wesley', 'Steven', 'Jennifer', 'Stephanie']

