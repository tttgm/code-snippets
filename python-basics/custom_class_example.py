### Example of a class ###

# Will create a class 'Point' that represents the (x, y) coordinates of a point.
# This class does not inherit from a superclass (which means it natively inherits from the 'object' superclass)
class Point:
	# 'special methods' are called with preceeding/trailing double underscores!
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def dist_from_origin(self):
		return math.hypot(self.x, self.y)

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __repr__(self):
		return "Point({0.x!r}, {0.y!r})".format(self)

	def __str__(self):
		return "({0.x!r}, {0.y!r})".format(self)

# These functions are all 'methods' available to any 'instance' of the Point class.

# The Point class has two 'data attributes', self.x and self.y, and 5 methods - 4 of which are 'special methods'

# Note that 'self' is the first argument in each method - this is because Python automatically supplies the first argument
# in method calls as an object reference to the object itself!
