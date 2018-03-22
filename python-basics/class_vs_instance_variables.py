### Class Variables vs Instance Variables ###

"""
OOP allows for not only methods (functions), but also variables to be declared at either the 'class' or 'instance' level.

When it's desirable that the variable will be constant/consistent across instances, we can define that variable at the class level.

When the variable will change depending on the instance, then it should instead be declared at the instance level.

Below are examples of both 'class' and 'instance' level variable declarations.

"""

# CLASS VARIABLE DECLARATION
# By convention, class variables are typically placed right below the class header and 
# before the 'constuctor' method (i.e. def '__init__'(self)).

# e.g.
class Shark:    # class called 'Shark' created
    animal_type = "fish"    # class variable 'animal_type' defined

    new_shark = Shark()     # create instantiation of class (i.e. Shark 'object')

    print(new_shark.animal_type)    # class variables can be accessed via dot-notation


### INSTANCE VARIABLE DECLARATION
# Instance variables are owned by the instances (objects) of the class.
# This means that for each instance of the class they can/will be different.

# Instance variables are therefore defined WITHIN methods (funcs) in the class definition.
# e.g.
class Shark:
    # create constructor method
    def __init__(self, name, age):
        self.name = name
        self.age = age

# In the example above, the instance variables 'name' and 'age' are INITIALIZED within
# the constructor method.
# Therefore, they require being passed as parameters when instantiating the instance of the class.
# The can still be accessed via the dot-notation.
# i.e.
new_shark = Shark("Tim", 36)    # create instance of Shark object, and pass two params (as 'name' and 'age' instance vars)
print(new_shark.name)
print(new_shark.age)    # can access variables by dot-notation

# We can also use both class and instance variables in the same class, including other,
# non-'constructor' instance variable declarations.
# e.g.
class Shark:
    # Class variables
    animal_type = "fish"
    location = "ocean"

    # Constructor method with instance variables 'name' and 'age'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method with instance variable 'followers'
    def set_followers(self, followers):
        print("This user has " + str(followers) + " followers.")

# Now create an instance of this class
sam = Shark("Sam", 13)  # name set to "Sam", age set to 13
print(sam.age) # Print out instance variable
print(sam.location) # Print out class variable
sam.set_followers(249) # use 'set_followers()' method and pass 'followers' instance variable

