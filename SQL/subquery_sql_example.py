### SUB-QUERIES IN SQL ###
'''
You can actually SELECT from the RESULTS of a SELECT QUERY. This is referred to as a SUB-QUERY.
Remember that the RESULT of a select query is always a (new) TABLE. This means that we can SELECT from this generated table as per a normal table.
The syntax of SQL requires that you give the sub-query table a NAME (i.e. AS table_name).
'''

#The most simple way of performing sub-queries is to put the whole SELECT statement inside backets hierarchically.
#e.g.
SELECT avg(bigscore)
FROM (
SELECT max(score) AS bigscore
FROM mooseball
GROUP BY team
)
AS maxes;   # need to name the sub-table

#Another example:

SELECT BillingCity, BillingState, BillingCountry, Total
FROM Invoice, (SELECT avg(Total) as average FROM Invoice) as subquery
WHERE Total > average;

# this JOINs the Invoice table to the table created in the subquery then compares the column 'Total' in the Invoice table directly to the column 'average' created in the joined table.
