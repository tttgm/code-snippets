### EXAMPLE SQL QUERY ###

QUERY = "SELECT FirstName, LastName, Title, Birthdate FROM Employee;"

#The above queries a database table 'Employee' and returns the values in the fields 'FirstName', 'LastName', 'Title', and 'Birthdate'.

#More complex query example:
#Example call from the tables in the database 'animals' above:

QUERY = '''
SELECT count(*) as number, species  # return two columns: 'number' (from count() aggregator) and 'species'
FROM animals    # from the 'animals' table
GROUP BY species    # group by the species (defines the 'bins' for the count() agg to operate on)
ORDER BY number DESC    # arrange in descending order
'''

'''
This returns a table with two columns: the species name and the total number of that species.
e.g.

__________________
|  Tiger  |  12  |
|  Zebra  |  6   |
|  Lion   |  4   |
|  Bear   |  1   |
'''