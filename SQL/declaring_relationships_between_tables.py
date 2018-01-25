### DECLARING RELATIONSHIPS BETWEEN TABLES ###

#'References' (as constraints) provide referential integrity - columns that are supposed to refer to each other are guaranteed to do so.

#We can establish references to other tables by using the 'references' keyword when creating new tables.

#e.g.
CREATE TABLE sales (
    sku text references products(id),
    sale_date date,
    count integer
);

# this creates a table called 'sales' with the columns 'sku', 'sale_date', and 'count'. The 'sku' column must also be a value in the table called 'products' in its 'id' column.
#Note: if the column name is the same in both tables that are referencing each other then you don't need to specify it. For example, if the 'products' table above had a 'sku' column it would be:
    
sku text references products,

#This is similar to a 'type check' in Python, and helps catch errors that might lead to problems later on with database manipulation.

'''
In database terminology, a column with a 'references constraint' on it is also called a FOREIGN KEY.

It is possible (and common) for a table to have 2 (or more) 'foreign key' columns.
'''
