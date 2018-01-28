##### Working with JSON data in Python #####

import json

json_data = open('data.json').read()

data = json.loads(json_data)    # note: the '.loads()' method expects a string, not a file.

for item in data:
    print item
