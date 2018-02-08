### Some example uses the 'os' module ###

# This is a program that finds duplicate files by 'walking' through the entire directory tree using os.walk()
# Creates a dict where each key is a tuple (file size, filename) and each value is a list of the full 
# filenames that match their key's filenames and have the same size.

from collections import defaultdict
import os

data = collections.defaultdict(list)

for root, dirs, files in os.walk(path):
	for filename in files:
		fullname = os.path.join(root, filename)
		key = (os.path.getsize(fullname), filename)
		data[key].append(full)

# Now to check for duplicates and generate readable output:
for size, filename in sorted(data):
	names = data[(size, filename)]
	if len(names) > 1:
		print("{0} ({1} bytes) may be duplicated "
			"({2} files):".format(filename, size, len(name)))
		for name in names:
			print("\t{0}".format(name))

# Note that this makes use of several functions available in the os module!
