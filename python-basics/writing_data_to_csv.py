### Writing data to csv

"""
	If we have a data file - e.g., 'zipped_data', containing a list of survey responses,
	with each survey containing a list of tuples in the form (question, answer), we can unpack
	it and write it to a .csv file using the following code.
"""

from csv import writer 	# use 'csv' library to get 'writer' method

def write_file(some_data, file_name):
	# use 'with...' syntax so that file will close automatically once operation is complete
	with open(file_name, 'wb') as new_csv_file: 	# 'wb' means 'write in binary mode'
		wrtr = writer(new_csv_file) 	# create 'writer' obj by passing in open file 'new_csv_file'
		titles = [row[0][1] for row in some_data[0]] 	# create the header row from the first entry in zipped_data

		# write the titles/headers row
		wrtr.writerow(titles) 	# use the '.writerow' method, which takes an iterable and returns a list of comma-separated entries

		# now write the rest of the data to to the 'wrtr' obj
		for row in some_data:
			answers = [resp[1] for resp in row] 	# use list comprehension to access second item of each tuple in the list 'row'
			wrtr.writerow(answers) 	# write them using the 'wrtr' obj

# now just call function on the desired dataset and provide a file name to be written to
write_file(zipped_data, 'cleaned_unicef_data.csv')

