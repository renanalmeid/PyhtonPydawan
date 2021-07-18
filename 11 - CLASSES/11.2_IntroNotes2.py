########## Constructors
#There are several methods that we can define in a Python class that have special behavior. These methods are sometimes called “magic,” because they behave differently from regular methods. 
#Another popular term is dunder methods, so-named because they have two underscores (double-underscore abbreviated to “dunder”) on either side of them.

#The first dunder method we’re going to use is the __init__() method (note the two underscores before and after the word “init”). 
#This method is used to initialize a newly created object. It is called every time the class is instantiated.

#Methods that are used to prepare an object being instantiated are called constructors. The word “constructor” is used to describe similar features in other object-oriented programming languages but programmers who refer to a constructor in Python are usually talking about the __init__() method.

#class Shouter:
#  def __init__(self):
#    print("HELLO?!")
 
#shout1 = Shouter()
# prints "HELLO?!"
 
#shout2 = Shouter()
# prints "HELLO?!"

#Above we created a class called Shouter and every time we create an instance of Shouter the program prints out a shout. Don’t worry, this doesn’t hurt the computer at all.

#Pay careful attention to the instantiation syntax we use. Shouter() looks a lot like a function call, doesn’t it? If it’s a function, can we pass parameters to it? We absolutely can, and those parameters will be received by the __init__() method.

#class Shouter:
#  def __init__(self, phrase):
    # make sure phrase is a string
#    if type(phrase) == str:
 
      # then shout it out
#      print(phrase.upper())
 
#shout1 = Shouter("shout")
# prints "SHOUT"
 
#shout2 = Shouter("shout")
# prints "SHOUT"
 
#shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"

#Above we’ve updated our Shouter class to take the additional parameter phrase. When we created each of our objects we passed an argument to the constructor. The constructor takes the argument phrase and, if it’s a string, prints out the all-caps version of phrase.

class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print("New circle with diameter: {diameter}".format(diameter=diameter))
    
teaching_table = Circle(36)

########### Instance Variables

#We’ve learned so far that a class is a schematic for a data type and an object is an instance of a class, 

#but why is there such a strong need to differentiate the two if each object can only have the methods and class variables the class has? This is because each instance of a class can hold different kinds of data.

#The data held by an object is referred to as an instance variable. Instance variables aren’t shared by all instances of a class — they are variables that are specific to the object they are attached to.

#class FakeDict:
#  pass

#We can instantiate two different objects from this class, fake_dict1 and fake_dict2, and assign instance variables to these objects using the same attribute notation that was used for accessing class variables.

#fake_dict1 = FakeDict()
#fake_dict2 = FakeDict()
 
#fake_dict1.fake_key = "This works!"
#fake_dict2.fake_key = "This too!"
 
# Let's join the two strings together!
#working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
#print(working_string)
# prints "This works! This too!"

class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"


######## Attribute Functions

#Instance variables and class variables are both accessed similarly in Python. This is no mistake, they are both considered attributes of an object. If we attempt to access an attribute that is neither a class variable nor an instance variable of the object Python will throw an AttributeError.

#class NoCustomAttributes:
#  pass
#attributeless = NoCustomAttributes()
 
#try:
#  attributeless.fake_attribute
#except AttributeError:
#  print("This text gets printed!") 
# prints "This text gets printed!"

#What if we aren’t sure if an object has an attribute or not? hasattr() will return True if an object has a given attribute and False otherwise. #If we want to get the actual value of the attribute, getattr() is a Python function that will return the value of a given object and attribute. #In this function, we can also supply a third argument that will be the default if the object does not have the given attribute.

## Syntax
#hasattr(object, “attribute”) has two parameters:
#object : the object we are testing to see if it has a certain attribute
#attribute : name of attribute we want to see if it exists

#getattr(object, “attribute”, default) has three parameters (one of which is optional):
#object : the object whose attribute we want to evaluate
#attribute : name of attribute we want to evaluate
#default : the value that is returned if the attribute does not exist (note: this parameter is optional)


#EXAMPLE

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

#For every element in the list, check if the element has the attribute count using the hasattr() function. If so, print the following line of code:

for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")


#This is because dictionaries and integers both do not have a count attribute, while strings and lists do. 


######### Self

#Since we can already use dictionaries to store key-value pairs, using objects for that purpose is not really useful. Instance variables are more powerful when you can guarantee a rigidity to the data the object is holding.

#This convenience is most apparent when the constructor creates the instance variables, using the arguments passed in to it. If we were creating a search engine, and we wanted to create classes for each separate entry we could return. We’d do that like this:

class SearchEngineEntry:
  def __init__(self, url):
    self.url = url
 
codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")
 
#print(codecademy.url)
# prints "www.codecademy.com"
 
#print(wikipedia.url)
# prints "www.wikipedia.org"

#Since the self keyword refers to the object and not the class being called, we can define a secure method on the SearchEngineEntry class that returns the secure link to an entry.

class SearchEngineEntry:
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url
 
  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)
 
codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")
 
#print(codecademy.secure())
# prints "https://www.codecademy.com"
 
#print(wikipedia.secure())
# prints "https://www.wikipedia.org"

#Above we define our secure() method to take just the one required argument, self. We access both the class variable self.secure_prefix and the instance variable self.url to return a secure URL.

#This is the strength of writing object-oriented programs. We can write our classes to structure the data that we need and write methods that will interact with that data in a meaningful way.

## Example 

class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    
    self.radius = diameter / 2
    
  def circumference(self):
    return 2 * self.pi * self.radius
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

########## Everything is an Object

#Attributes can be added to user-defined objects after instantiation, so it’s possible for an object to have some attributes that are not explicitly defined in an object’s constructor. 
#We can use the dir() function to investigate an object’s attributes at runtime. dir() is short for directory and offers an organized presentation of object attributes.

class FakeDict:
  pass
 
fake_dict = FakeDict()
fake_dict.attribute = "Cool"
 
#dir(fake_dict)

#Do you remember being able to use type() on Python’s native data types? This is because they are also objects in Python. 

#Their classes are int, float, str, list, and dict. These Python classes have special syntax for their instantiation, 1, 1.0, "hello", [], and {} specifically. But these instances are still full-blown objects to Python.

dir(5)

def this_function_is_an_object(any): 
  return any

print(dir(this_function_is_an_object))


######### String Representation
#One of the first things we learn as programmers is how to print out information that we need for debugging. Unfortunately, when we print out an object we get a default representation that seems fairly useless.

#This default string representation gives us some information, like where the class is defined and our computer’s memory address where this object is stored, but is usually not useful information to have when we are trying to debug our code.

#We learned about the dunder method __init__(). Now, we will learn another dunder method called __repr__(). This is a method we can use to tell Python what we want the string representation of the class to be. __repr__() can only have one parameter, self, and must return a string.
class Employee():
  def __init__(self, name):
    self.name = name
 
  def __repr__(self):
    return self.name
 
argus = Employee("Argus Filch")
print(argus)
# prints "Argus Filch"



class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
 # def __repr_(self):
  #  teste = print("Circle with radius {radius}".format(radius.self = radius))
 #   return teste
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)