from datetime import datetime as dt

# Takes a date as a string, and returns a Python datetime object. 
# If there is no date given, returns None.

def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')

# Can convert normal text into a datetime object via string indexing
# This can be stored as a 'datetime object' with the .strptime() method
# e.g.

sentence = "We met at 11:55 pm on 23/4/2015."

formatted_time = "{}/{}/{} {}:{}".format(
    sentence[-10:-8], sentence[-7], sentence[-5:-1],
    sentence[10:12], sentence[13:15]
    )

print formatted_time  # is now a formatted str

formatted_datetime = dt.strptime(formatted_time, '%d/%m/%Y %H:%M')

print formatted_datetime   # is now a datetime obj
