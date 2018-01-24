### OPENING DATABASE FILES AND WORKING WITH SQLITE IN TERMINAL ###

#Move to the directory with the file_name.db file in it.
#Run:
sqlite3 file_name.db

#This will open sql in the terminal, you should see a new prompt:
sqlite>


#Common SQL commands:

sqlite> .help       # run at any time to find details about database functions

sqlite> .tables     # see what tables are in your database

sqlite> .schema table_name      # returns information about the table 'table_name'

#The key info that gets returned from .schema is:
CREATE TABLE [Album] # <-- This is the table name, Album.

[AlbumId] # <---These are your column names, this table has 3: 'AlbumID', 'Title', and 'ArtistID'
[Title]
[ArtistId]

    INTEGER,       # <---Next are the datatypes for each column
    NVARCHAR(160), 
    INTEGER,

#If you don't specifiy a table then .schema returns information about ALL of the tables in the database.

#Some example queries:

sqlite> SELECT * FROM table_name;       # returns all the data in the 'table_name' table

#SQL supports boolean 'AND' 'OR' 'NOT' logical operators.
#e.g.
SELECT name FROM animals WHERE (NOT species=guerilla) AND (NOT name='Max')

#Could also use the '!=' operator in the case above.

#The QUERY format:

#Can put the 'SELECT * FROM * WHERE *' query inside double quotes, and assign it to a variable QUERY and it will run as per normal.
#i.e.
QUERY = " SELECT speed FROM animals WHERE species='Tiger' "

#OTHER SQL COMMANDS (called 'Select clauses')

'ORDER BY' - sets order in column (default is ascending, add 'DESC' to output descending order)
'GROUP BY' - groups subsets within columns together (e.g. to use with min()/sum() functions etc)
'LIMIT XX' - limits to the first 'XX' entries (e.g. 'LIMIT 10' provides first 10 entries)
'OFFSET XX' - starts after 'XX' rows. Most used with 'limit' - e.g. 'LIMIT 10 OFFSET 50' (starts from row 50 and returns 10 rows)
'AS' - set a name for a newly returned column

