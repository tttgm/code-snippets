### An example of class inheritance ###

# Here we are going to create a new custom class 'Circle' which inherits the (x, y) coordinates 
# from the previously-defined 'Point' class

# The super/base class to inherit from is passed as an argument in the class definition
class Circle(Point):

	# Can then 'reimplement' (i.e. override) some of the class methods, as well as introduce new methods.
	def __init__(self, radius, x=0, y=0):
		super().__init__(x, y) 	# this calls the '__init__()' method of the super-class to initialize x and y
		self.radius = radius 	# as 'radius' is a new attribute we must initialize it here (note: no default value is given)

	# How about creating a few new Circle()-only method
	def edge_dist_from_origin(self):
		return abs(self.edge_dist_from_origin() - self.radius)

	def circumference(self):
		return 2 * math.pi * self.radius

	# Can also 'reimplement' some of the other 'special methods'
	def __eq__(self, other):
		return self.radius == other.radius and super().__eq__(other) 	
		# check equality while also calling the super-class eq() method on the 'other' argument

	def __str__(self):
		return repr(self)
		# this needs to be reimplemented so that the str returned represents a CIRCLE rather than just a POINT

