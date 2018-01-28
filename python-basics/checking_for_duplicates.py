### Checking for duplicates and eliminating duplicates ###

"""
	Duplicate entries in a dataset may not be valid or just might not be required.

	Python can easily elim the duplicates in a list using the 'set()' data storage type.

	Note: set() method can take an iterable such as a list, a string, or a tuple.

	Set 'look-up' and comparisons are also extremely fast.

	We can also use sets to perform Venn-diagram type operations (e.g. 'intersection', 'union', etc.) easily
	with several built-in functions.

"""

# Convert list to a set with no double-entries
list_with_duplicates = [1, 5, 6, 2, 5, 6, 8, 9, 3, 3, 7, 9]
set_without_duplicates = set(list_with_duplicates)

print set_without_duplicates

# Perform Venn-diagram/merging operations on lists/sets
first_set = set([1, 5, 6, 2, 6, 3, 6, 7, 3, 7, 9, 10, 321, 54, 654, 432])
second_set = set([4, 6, 7, 432, 6, 7, 4, 9, 0])

print first_set.intersection(second_set) 	# returns all the elements held in common between the two sets
print first_set.union(second_set) 	# returns ALL elements in both sets
print first_set.difference(second_set) 	# returns the difference by subtracting any values from the first set that appear in the second set

print second_set - first_set  # this is kind of the inverse of the above method -- i.e., the ORDER matters!

# Quick membership test
print 6 in second_set
# >>> TRUE

print 81 in first_set
# >>> FALSE
