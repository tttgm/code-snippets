### JOINING TABLES ON A COMMON COLUMN ###

#Simple structure for a 'join' statement:

SELECT T.thing, S.stuff FROM T, S WHERE T.target = S.match and T.something = something
# adds the tables 'T' and 'S' on the 'target/match' columns. The last part is where the desired condition/restriction.


#NOTE that the WHERE command filters the SOURCE TABLE - i.e., the condition will be checked BEFORE any operations such as count() of max() have been applied.
#To filter the results of any aggregation operations we can use the HAVING command.

#e.g.
SELECT species, count(*) as num FROM animals GROUP BY species HAVING num = 1
# will return any species for which the count ('num') is equal to 1.
