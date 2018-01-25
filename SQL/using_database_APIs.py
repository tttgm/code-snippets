### USING DataBase-APIs ###

#The code operating in the background to make the connections to the database is actually often written in Python, and is called the 'DB-API' - i.e. the protocol for how to fetch, sort, analyze, and present data from a given database.

#A basic exmple of a DB-API is as follows:

import sqlite3      # imports the library for the database you want to use

conn = sqlite3.connect("Cookies")   # returns a 'connection object': makes a connection to the database called "Cookies". Note: if the database was accessed over a network you'd need the full URL address here. This connection will stay 'open' until it is closed by .close() (see below)

cursor = conn.cursor()  # establishes a 'cursor' that is used to move through the database on demand

query = "SELECT host_key FROM cookies LIMIT 10"     # basic SQL operation

cursor.execute(query)   # performs the SQL operation described in the 'query' statement above

results = cursor.fetchall()     # 'fetches' all the data sourced by the 'execute' call above. Can also use .fetchone() to fetch the results one at a time.

print results       # prints the data

conn.close()    # closes the connection to the database

# on the connection object, functions like .commit() and .rollback() are also common.

#If you make changes to a database (such as insert rows, update values etc) WITHOUT .commit()'ing the changes won't take effect if you close the connection - i.e. the database will be rolled back to its previous state.
