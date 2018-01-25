### IMPORT SQL TABLES INTO PANDAS DATAFRAMES ###

#You can easily import a sql table data into a Pandas df object using Python in the DB-API code.

#For example, if you save the .fetchall() data in something like:
rows = c.fetchall()

#you can easily convert to a df by using:

import pandas as pd
df = pd.DataFrame(rows)
print df

# will output data as structured df object