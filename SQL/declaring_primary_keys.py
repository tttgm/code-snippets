### DECLARING PRIMARY KEYS ###

#To set columns as a 'primary key' for the table - for a 'single column key':
#e.g.
CREATE TABLE students (     # creates a table called 'students'
    id serial primary key,  # creates column 'id' of type=serial and sets as 'primary key'
    name text,              # creates column 'name' of type=text
    birthdate date          # creates column 'birthdate' of type=date
);

#For a 'multi-column primary key' put AFTER ALL COLUMNS in the table as follows:
#e.g.
CREATE TABLE postal_places (
    postal_code text,
    country text,
    name text,
    primary key (postal_code, country)
);

# this sets the 'postal_code' and 'country' columns as the 'primary key' for the table 'postal_places'
