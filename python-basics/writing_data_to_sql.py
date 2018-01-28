### Saving data to a SQLite database

"""
	If we have a data file - e.g., 'zipped_data', containing a list of survey responses,
	with each survey containing a list of tuples in the form (question, answer), we can unpack
	it and save it to a newly created table in a SQLite database using the following code.
"""

import dataset 	# import 'dataset' module containing sql commands

# Connect to the database -- in this case a local database called 'data_wrangling.db'
db = dataset.connect('sqlite:///data_wrangling.db')

table = db['unicef_survey'] 	# create new table in the sql database db

for row_num, data in enumerate(zipped_data): 	# use enumerate to keep track of the 'row number'
	for question, answer in data: 	# unpack each tuple in the list with a for loop
		data_dict = { 		# assign key-value pairs into a new dictionary 'data_dict'
			'question': question[1],
			'question_code': question[0],
			'answer': answer,
			'response_number': row_num,
		}

table.insert(data_dict) 	# add that processed dictionary to the table in the database