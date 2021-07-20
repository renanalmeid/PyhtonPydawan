########### Using none as sentinel 
#So if we can’t use a list as a default argument for a function, what can we use? If we want an empty list, we can use None as a special value to indicate we did not receive anything. After we check whether an argument was provided we can instantiate a new list if it wasn’t.
def update_order(new_item, current_order=None):
  if current_order is None: 
    current_order = []
    
  current_order.append(new_item)
  return current_order

# First order, burger and a soda
order1 = update_order({'item': 'burger', 'cost': '3.50'})
order1 = update_order({'item': 'soda', 'cost': '1.50'}, order1)

# Second order, just a soda
order2 = update_order({'item': 'soda', 'cost': '1.50'})

# What's in that second order again?
print(order2)


########### Unpacking Multiple Returns 
#What if we wanted to save these two results in separate variables? Well we can by unpacking the function return. We can list our new variables, comma-separated, that correspond to the number of values returned:
def multiple_returns(cool_num1, cool_num2):
  sum_nums = cool_num1 + cool_num2
  div_nums = cool_num1 / cool_num2
  return sum_nums, div_nums

sum, div = multiple_returns(18, 9)
 
print(sum)
# Prints "27"
 
print(div)
# Prints "2"

def scream_and_whisper(text):
    scream = text.upper()
    whisper = text.lower()
    return scream, whisper

the_scream, the_whisper = scream_and_whisper("ALoww")

print(the_scream)
print(the_whisper)

########### Positional Argument Unpacking 
#The first method is called positional argument unpacking, because it unpacks arguments given by position. 
def shout_strings(*args):
  for argument in args:
    print(argument.upper())
 
shout_strings("hi", "what do we have here", "cool, thanks!")
# Prints out:
# "HI"
# "WHAT DO WE HAVE HERE"
# "COOL, THANKS!"
#In shout_strings() we use a single asterisk (*) to indicate we’ll accept any number of positional arguments passed to the function. Our parameter args is a tuple of all of the arguments passed. In this case args has three values inside, but it can have many more (or fewer).


def truncate_sentences(length, *sentences):
  for sentence in sentences:
    print(sentence[:length])
 
truncate_sentences(8, "What's going on here", "Looks like we've been cut off")
# Prints out:
# "What's g"
# "Looks li"

### example
from os.path import join

path_segment_1 = "/Home/User"
path_segment_2 = "Codecademy/videos"
path_segment_3 = "cat_videos/surprised_cat.mp4"

# join all three of the paths here!
print(join(path_segment_1, path_segment_2, path_segment_3))

def myjoin(*args):
  joined_string = args[0]
  for arg in args[1:]:
    joined_string += '/' + arg
  return joined_string

print(myjoin(path_segment_1, path_segment_2, path_segment_3))

########### Keyword Argument Unpacking
#Python doesn’t stop at allowing us to accept unlimited positional parameters, it gives us the power to define functions with unlimited keyword parameters too.
#The syntax is very similar, but uses two asterisks (**) instead of one. Instead of args, we call this kwargs — as a shorthand for keyword arguments.
def arbitrary_keyword_args(**kwargs):
  print(type(kwargs))
  print(kwargs)
  # See if there's an "anything_goes" keyword arg
  # and print it
  print(kwargs.get('anything_goes'))
 
arbitrary_keyword_args(this_arg="wowzers", anything_goes=101)
# Prints "<class 'dict'>
# Prints "{'this_arg': 'wowzers', 'anything_goes': 101}"
# Prints "101"

#As you can see, **kwargs gives us a dictionary with all the keyword arguments that were passed to arbitrary_keyword_args. We can access these arguments using standard dictionary methods.
#Since we’re not sure whether a keyword argument will exist, it’s probably best to use the dictionary’s .get() method to safely retrieve the keyword argument. Do you remember what .get() returns if the key is not in the dictionary? It’s None!

# Checkpoint 1
print("My name is {name} and I'm feeling {feeling}.".format(
	name = "Renan", feeling = "confused"
))

# Checkpoint 2
from products import create_product

# Update create_products() to take arbitrary keyword arguments
def create_products(**products_dict):
  for name, price in products_dict.items():
    create_product(name, price)

# Checkpoint 3
# Update the call to `create_products()` to pass in this dictionary as a series of keyword
create_products(Baseball=3, Shirt=14,Guitar=70)


###########  Using both keyword and positional Unpacking 
#All named positional parameters
#An unpacked positional parameter (*args)
#All named keyword parameters
#An unpacked keyword parameter (**kwargs)
def main(filename, *args, user_list=None, **kwargs):
  if user_list is None:
    user_list = []
 
  if '-a' in args:
    user_list = all_users()
 
  if kwargs.get('active'):
    user_list = [user for user_list if user.active]
 
  with open(filename) as user_file:
    user_file.write(user_list)


#example
def remove(filename, *args, **kwargs):
  with open(filename) as file_obj:
    text = file_obj.read()
  for arg in args:
    text = text.replace(arg, "")
  for kwarg, replacement in kwargs.items():
    text = text.replace(kwarg, replacement)
  return text

print(remove("text.txt", "generous", "gallant", fond="amused by", Robin="Mr. Robin"))


########### Passing Containers as Arguments
#Not only can we accept arbitrarily many parameters to a function in our definition, but Python also supports a syntax that makes deconstructing any data that you have on hand to feed into a function that accepts these kinds of unpacked arguments. 
# The syntax is very similar, but is used when a function is called, not when it’s defined.
def takes_many_args(*args):
  print(','.join(args))
 
long_list_of_args = [145, "Mexico City", 10.9, "85C"]
 
# We can use the asterisk "*" to deconstruct the container.
# This makes it so that instead of a list, a series of four different
# positional arguments are passed to the function
takes_many_args(*long_list_of_args)
# Prints "145,Mexico City,10.9,85C"

#We can use the * when calling the function that takes a series of positional parameters to unwrap a list or a tuple.
#This makes it easy to provide a sequence of arguments to a function even if that function doesn’t take a list as an argument. Similarly we can use ** to destructure a dictionary.

def pour_from_sink(temperature="Warm", flow="Medium")
  set_temperature(temperature)
  set_flow(flow)
  open_sink()
 
# Our function takes two keyword arguments
# If we make a dictionary with their parameter names...
sink_open_kwargs = {
  'temperature': 'Hot',
  'flow': "Slight",
}
 
# We can destructure them and pass to the function
pour_from_sink(**sink_open_kwargs)
# Equivalent to the following:
# pour_from_sink(temperature="Hot", flow="Slight")


##example
from products import create_product

def create_products(**products_dict):
  for name, price in products_dict.items():
    create_product(name, price)

new_product_dict = {
  'Apple': 1,
  'Ice Cream': 3,
  'Chocolate': 5,
}

# Call create_products() by passing new_product_dict
# as kwargs!

create_products(**new_product_dict)


