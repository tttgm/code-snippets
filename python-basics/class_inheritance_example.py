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

### Another example of class inheritance ###

# We'll code up two classes:
# 	- 'Person': a class to create and process info or characteristics about people
# 	- 'Manager': a sub-class of Person that has some additional or modified (inherited) behaviour.

# Define the 'Person' class
class Person:
	# The usual way to give a class instance their first values is to assign them to 'self' in the 
	# '__init__' constructor method, as this code will be run automatically by Python on instantiation.
	def __init__(self, name, job=None, pay=0): 	# constructor method takes 3 arguments. Setting default vals for 'job' and 'pay' make these arguments OPTIONAL.
		self.name = name
		self.job = job
		self.pay = pay

	# Create custom methods to provide 'encapsulation' - i.e., shared functionality/logic across all instances of this class
	def lastName(self):
		return self.name.split()[-1]

	# Can test that argument passed is acceptable (e.g. in this case, percent must be a float between 0 and 1)
	# by using 'function decorators'!
	@rangetest(percent=(0.0, 1.0)) 	# decorators are created with the prefixing '@' syntax
	def giveRaise(self, percent): 	# allow for pay rise percentage to be entered each time the method is called
		self.pay = int(self.pay * (1 + percent)) 


# Now let's create a sub-class of 'Person' to demonstrate some aspects of class inheritance.
# We'll create a class called 'Manager' which inherits from 'Person'
class Manager(Person):
	# In this case, it is desirable to modify the __init__ constructor from the Person super-class such
	# that the 'job' parameter is set to 'mgr' (as any obj of 'Manager' class should have the job title of 'manager').
	# We can extend the functionality of the Person.__init__() constructor method by calling it directly,
	# and passing the string value 'mgr' as the 'job' argument.
	# i.e.
	def __init__(self, name, pay):
		Person.__init__(self, name, 'mgr', pay)

	# We want to modify the 'giveRaise()' method for the Manager class such that manager's get an additional 10% raise.
	# The best way to do that is to actually CALL the parent class method - that way any changes in the
	# root method will be propagated to the child classes (i.e. less code maintanence problems).
	# i.e.
	def giveRaise(self, percent, bonus=0.1):	# 'bonus' is set to 0.1 to represent the additional 10% raise
		Person.giveRaise(self, percent + bonus) # here the 'percent + bonus' is passed to the parent classes 'percent' argument for the giveRaise() method
		# This way, 'bonus' can be sepcified (e.g. object.giveRaise(0.2, 0.4) - where 20% is the initial raise and 40% is the bonus),
		# but it will default to 10%.

