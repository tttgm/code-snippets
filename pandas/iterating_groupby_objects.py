### Iterating over groupby objects ###

'''
Can access the data hidden within the 'groupby objects' to extract the group 'names' and values (within
each group usually stored in a sub-dataframe).

A common use of this code is shown, where the grouped data is extracted into a dict with the group names
as the keys.

'''

from pandas import DataFrame
df = DataFrame({'Team': ['DEN', 'TOR', 'POR', 'POR', 'DEN', 'TOR', 'POR', 'OKC', 'DEN', 'UTA'],
      'Player': ['Harris', 'Lowry', 'Lillard', 'McCollum', 'Jokic', 'DeRozan', 'Nurkic', 'Westbrook', 'Murray', 'Mitchell'],
      'rating': np.random.randint(100, size=10),
      'score': np.random.randint(100, size=10)})


# To get the group name, and the data within it, use var unpacking:
for name, group in df.groupby('Team'):
    print(name)
    print(group)

->  DEN
       Player Team  rating  score
    0  Harris  DEN      82     57
    4   Jokic  DEN       4     63
    8  Murray  DEN      55     40
    OKC
          Player Team  rating  score
    7  Westbrook  OKC      92      8
    POR
         Player Team  rating  score
    2   Lillard  POR      82     99
    3  McCollum  POR      29     15
    6    Nurkic  POR      80     59
    TOR
        Player Team  rating  score
    1    Lowry  TOR      10     70
    5  DeRozan  TOR      37     76
    UTA
         Player Team  rating  score
    9  Mitchell  UTA      32     89


# If there are MULTIPLE keys in the groupby (i.e. hierarchical structure), the first element in the unpacking
# step will be a TUPLE.
# i.e.
for (key1, key2), group in df.groupby(['Team', 'Player']):
    print(key1, key2)
    print(group)

->  DEN Harris
       Player Team  rating  score
    0  Harris  DEN      82     57
    DEN Jokic
      Player Team  rating  score
    4  Jokic  DEN       4     63
    DEN Murray
       Player Team  rating  score
    8  Murray  DEN      55     40
    OKC Westbrook
          Player Team  rating  score
    7  Westbrook  OKC      92      8
    POR Lillard
        Player Team  rating  score
    2  Lillard  POR      82     99
    POR McCollum
         Player Team  rating  score
    3  McCollum  POR      29     15
    POR Nurkic
       Player Team  rating  score
    6  Nurkic  POR      80     59
    TOR DeRozan
        Player Team  rating  score
    5  DeRozan  TOR      37     76
    TOR Lowry
      Player Team  rating  score
    1  Lowry  TOR      10     70
    UTA Mitchell
         Player Team  rating  score
    9  Mitchell  UTA      32     89


# To store these obj's in a python dict, can perform the following
group_dict = dict(list(df.groupby('Team')))

group_dict['DEN']
->  x   Player  Team    rating  score
    0   Harris  DEN     82      57
    4   Jokic   DEN     4       63
    8   Murray  DEN     55      40


