### Dictionary creation and default values ###

# When setting values in a dict, it is common to want to set the value as another collection (e.g. list, tuple, dict).

# For example, say you want to categorize a list of words by their first letters as a dict-of-lists;
# this can be achieved by the following code:

words = ['apple', 'bat', 'bar', 'atom', 'book']

by_letter = {}  # empty dict to store lists
for word in words:
    letter = word[0]    # fetch first letter of word
    if letter not in by_letter:
        by_letter[letter] = [word]      # create dict value as list with one entry, 'word'
    else:
        by_letter[letter].append(word)  # if letter already a key in the dict, append the word to the value (list) already there

# This works fine, but there are more simple ways to achieve the same thing by using the 'defaultdict' from
# the 'collections' module.

# A 'defaultdict' is created by passing a type (or function) to act as the default value for any dict entry:
from collections import defaultdict
by_letter = defaultdict(list)   # create dict and set 'list' as the default value (i.e. an empty list)
for word in words:
    by_letter[word[0]].append(word)     # add words to the list!

# Alternatively, you can set a default VALUE (not type) by using a lambda function:
# e.g.
counts = defaultdict(lambda: 4)     # all keys created will have a default value of 4
