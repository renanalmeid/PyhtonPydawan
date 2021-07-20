########### Parameters and Arguments
#Python’s functions offer us a very expressive syntax. We’re going to look into some of the finer details of how functions in Python work and some techniques we can use to be more intuitive while writing and calling functions.
#A parameter is a variable in the definition of a function.
#An argument is the value being passed into a function call.
#A function definition begins with def and contains the entire following indented block.
#And function calls are the places a function is invoked, with parentheses, after its definition

from record_library import place_record, rotate_record, drop_needle

def play_record(album):
  place_record(album)
  rotate_record(album)
  drop_needle(album)

next_album = "Blondie / Parallel Lines"

play_record(next_album)


########### None: Its Nothing 
#None is falsy, meaning that it evaluates to False in an if statement, which is why the above code prints “Goodbye”. None is also unique, which means that you can test if something is None using the is keyword.
from review_lib import get_next_review, submit_review


review = get_next_review()

if review is not None: 
  submit_review(review)


########### Default Return 
#A Python function that does not have any explicit return statement will return None after completing. This means that all functions in Python return something, whether it’s explicit or not.
# store the result of this print() statement in the variable prints_return
print("What does this print function return?")

# print out the value of prints_return
prints_return = print("hi!")

print(prints_return)
# call sort_this_list.sort() and save that in list_sort_return
sort_this_list = [14, 631, 4, 51358, 50000000]

list_sort_return = sort_this_list.sort()
# print out the value of list_sort_return


print(list_sort_return) 


########### DefaultArguments 
import os

def make_folders(folders_list, nest =  False):
  if nest:
    """
    Nest all the folders, like
    ./Music/fun/parliament
    """
    path_to_new_folder = "."
    for folder in folders_list:
      path_to_new_folder += "/{}".format(folder)
      try:
        print(path_to_new_folder)
        os.makedirs("./" + path_to_new_folder)
      except FileExistsError:
        continue
  else:
    """
    Makes all different folders, like
    ./Music/ ./fun/ and ./parliament/
    """
    for folder in folders_list:
      try:
        os.makedirs(folder)

      except FileExistsError:
        continue

make_folders(['Music', 'fun', 'parliament'])


########### Using Keywortd and Positional Arguments
#Not all of your arguments need to have default values. But Python will only accept functions defined with their parameters in a specific order. The required parameters need to occur before any parameters with a default argument.
import reqs as requests
from bs4 import BeautifulSoup

def get_id(html_id, website="http://coolsite.com"):
  request = requests.get(website)
  parsed_html = BeautifulSoup(website.content, features="html.parser")
  return parsed_html.find(id_=html_id)



########### Keyword Arguments
import shapes

def draw_shape(shape_name="box", character="x", line_breaks=True):
  shape = shapes.draw_shape(shape_name, character)
  if not line_breaks:
    print(shape[1:-1])
  else:
    print(shape)

# call draw_shape() with keyword arguments here:

draw_shape(character = "m", line_breaks = False)


########### Dont use Mutable Default Arguments
 
def update_order(new_item, current_order=[]):
  current_order.append(new_item)
  return current_order

# First order, burger and a soda
order1 = update_order({'item': 'burger', 'cost': '3.50'})
order1 = update_order({'item': 'soda', 'cost': '1.50'}, order1)

# Second order, just a soda
order2 = update_order({'item': 'soda', 'cost': '1.50'})

# What's in that second order again?
print(order2)
