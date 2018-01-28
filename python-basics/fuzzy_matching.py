### "Fuzzy matching" of strings ###

"""
	A library written by SeatGeek provides some convenient functions for "fuzzy" string matching.
	For example, we might want to relate "My dog & I" with "Me and my dog", but without having to
	use extensive natural language processing or machine learning.

	The library is called 'fuzzywuzzy', you might need to install it:

		pip install fuzzywuzzy

"""

# some examples

from fuzzywuzzy import fuzz

# Say we have some string entries, but the spellings are slightly inconsistent.
# Can use the 'fuzz' modules 'ratio' function to assess the similarity
# between two strings - given as a number between 1 and 100.

my_records = [{'favorite_book': 'Grapes of Wrath',
				'favorite_movie': 'Free Willie',
				'favorite_show': 'Two Broke Girls',
				},
				{'favorite_book': 'The Grapes of Wrath',
				'favorite_movie': 'Free Willy',
				'favorite_show': '2 Broke Girls',
				}]

# Use the .ratio function to compare entries in the above list-of-dicts

print fuzz.ratio(my_records[0].get('favorite_book'),
				my_records[1].get('favorite_book'))

print fuzz.ratio(my_records[0].get('favorite_movie'),
				my_records[1].get('favorite_movie'))

print fuzz.ratio(my_records[0].get('favorite_show'),
				my_records[1].get('favorite_show'))

# Alternatively, can use the 'partial_ratio' function which searches SUB-STRINGS within the 
# entry, and so the effects of additional words (e.g. 'The' in the second book entry above)
# less impacting on the ratio result (again, given as a no. between 1 and 100).

print fuzz.partial_ratio(my_records[0].get('favorite_book'),
				my_records[1].get('favorite_book'))

print fuzz.partial_ratio(my_records[0].get('favorite_movie'),
				my_records[1].get('favorite_movie'))

print fuzz.partial_ratio(my_records[0].get('favorite_show'),
				my_records[1].get('favorite_show'))

# There are many more functions available in fuzzywuzzy -- see docs for further info.
