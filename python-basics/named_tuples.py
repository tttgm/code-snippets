### Named tuples ###

"""
	Can use the 'namedtuple()' method from the 'collections' library to give a name to each entry in a tuple.
	This makes accessing the entries much more readable than just using indexing.
"""
# e.g.

import collections

# the first parameter is the tuple NAME, followed by a space-separated string of the names for each entry
Aircraft = collections.namedtuple("Aircraft", "manufacturer model seating")
Seating = collections.namedtuple("Seating", "minimum maximum")

# create the tuples using their assigned names
aircraft = Aircraft("Airbus", "A320-200", Seating(100, 220))

# access the tuple elements by calling their entry name using dot-notation
print aircraft.seating.maximum

# >>> 220
