### PARSING CSV'S WITH DICTREADER ###

import csv

def parse_csv('datafile.csv'):

    data = []

    with open('datafile.csv', 'r') as f:
        g = csv.DictReader(f)   # DictReader() sets the values in the first row as 'column headers'
        for line in g:
            data.append(line)

    return data
'''
This function generates an list-of-dicts that contain key:value pairs, where the keys are the entries in the FIRST ROW of the csv file, and the values are then matched up by index.
'''