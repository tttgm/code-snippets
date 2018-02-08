### Dictionary iterations ###

"""
	Dict's are iterable, so can use many of the same methods as for lists.

	Also, can extract keys and/or values with .values() and .keys() methods.

"""

ppg = { "Melo": 25.6, "Harden": 28.9, "LeBron": 27.7, "Steph": 30.1, "Russ": 22.3, "Jokic": 17.6 }

# Can access both the keys and values
for i in ppg.items():
	print (i[0], i[1])
    
# >>> ('Jokic', 17.6), ('Steph', 30.1), ('Harden', 28.9), ('Melo', 25.6), ('Russ', 22.3), ('LeBron', 27.7)

# or get the same result using
for key, value in ppg.items():
	print (key, value)

# >>> ('Jokic', 17.6), ('Steph', 30.1), ('Harden', 28.9), ('Melo', 25.6), ('Russ', 22.3), ('LeBron', 27.7)


# Can get just the VALUES
for value in ppg.values():
	print value

# >>> 17.6, 30.1, 28.9, 25.6, 22.3, 27.7

# Can get just the KEYS using
for key in ppg:
	print key

# or
for key in ppg.keys():
	print key

# >>> Jokic, Steph, Harden, Melo, Russ, LeBron

