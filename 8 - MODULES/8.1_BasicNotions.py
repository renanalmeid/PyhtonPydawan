########### INTRODUCTION
# we’ll explore how to use tools other people have built in Python that are not included automatically for you when you install Python

#Python allows us to package code into files or sets of files called modules.

#A module is a collection of Python declarations intended broadly to be used as a tool.

#Modules are also often referred to as “libraries” or “packages” — a package is really a directory that holds a collection of modules.

#Example
#from module_name import object_name

#One common library that comes as part of the Python Standard Library is datetime. datetime helps you work with dates and times in Python.
from datetime import datetime

current_time = datetime.now()
print(current_time)


###########Modules Python Random
#Another one of the most commonly used is random which allows you to generate numbers or select items at random.

#With random, we’ll be using more than one piece of the module’s functionality, so the import syntax will look like:

#import random
#random.choice() which takes a list as an argument and returns a number from the list
#random.randint() which takes two numbers as arguments and generates a random number between the two numbers you passed in


# Import random below:
import random

# Create random_list below:
random_list =[]
# Create randomer_number below:
#Turn the empty list into a list comprehension that uses random.randint() to generate a random integer between 1 and 100 (inclusive) for each number in range(101).
random_list = [random.randint(1,100) for index in range(101)]
randomer_number = random.choice(random_list)
print(randomer_number)

########## Modules Python Namespaces
#Notice that when we want to invoke the randint() function we call random.randint(). This is default behavior where Python offers a namespace for the module.

#A namespace isolates the functions, classes, and variables defined in the module from the code in the file doing the importing. Your local namespace, meanwhile, is where your code is run.

#Aliasing is most often done if the name of the library is long and typing the full name every time you want to use one of its functions is laborious.

#You might also occasionally encounter import *. The * is known as a “wildcard” and matches anything and everything. This syntax is considered dangerous because it could pollute our local namespace.

#Pollution occurs when the same name could apply to two possible things.

#matplotlib, which allows you to plot your Python code in 2D.

import codecademylib3_seaborn
from matplotlib import pyplot as plt
import random 

numbers_a = range(1,13)

#sample primeiro argumento range segundo qnts numeros sao retirados
numbers_b = random.sample(range(1000), 12)

plt.plot(numbers_a,numbers_b)

plt.show()
