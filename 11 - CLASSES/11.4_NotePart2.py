###############Inheritance

class Bin:
  pass

class RecyclingBin(Bin):
  pass

############# Exceptions
# Define your exception up here:
class OutOfStock(Exception):
  pass

# Update the class below to raise OutOfStock
class CandleShop:
  name = "Here's a Hot Tip: Buy Drip Candles"
  def __init__(self, stock):
    self.stock = stock
    
  def buy(self, color):
    if self.stock[color] < 1:
      raise OutOfStock
    self.stock[color] = self.stock[color] - 1

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# This should raise OutOfStock:
candle_shop.buy('green')

########### Overriding Methods

class Message:
  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text

class User:
  def __init__(self, username):
    self.username = username
    
  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text

class Admin(User):
  def edit_message(self, message, new_text):
   message.text = new_text

############## super()

class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions
    
class SpecialPotatoSalad(PotatoSalad):
  def __init__(self, potatoes, celery, onions):
    super().__init__(potatoes, celery, onions)
    self.raisins = 40


########################## Interfaces

class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item

class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    return 0.001 * self.price_of_insured_item

class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return 0.00005 * self.price_of_insured_item

# Example 2
class Chess:
  def __init__(self):
    self.board = setup_board()
    self.pieces = add_chess_pieces()
 
  def play(self):
    print("Playing chess!")
 
class Checkers:
  def __init__(self):
    self.board = setup_board()
    self.pieces = add_checkers_pieces()
 
  def play(self):
    print("Playing checkers!")

class Chess:
  def __init__(self):
    self.board = setup_board()
    self.pieces = add_chess_pieces()
 
  def play(self):
    print("Playing chess!")
 
class Checkers:
  def __init__(self):
    self.board = setup_board()
    self.pieces = add_checkers_pieces()
 
  def play(self):
    print("Playing checkers!")



###############  Dunder Methods

#example1
class Color:
  def __init__(self, red, green, blue):
    self.red = red
    self.green = green
    self.blue = blue
 
 
  def __repr__(self):
    return "Color with RGB = ({red}, {green}, {blue})".format(red=self.red, green=self.green, blue=self.blue)
 
  def add(self, other):
    """
    Adds two RGB colors together
    Maximum value is 255
    """
    new_red = min(self.red + other.red, 255)
    new_green = min(self.green + other.green, 255)
    new_blue = min(self.blue + other.blue, 255)
 
    return Color(new_red, new_green, new_blue)
 
red = Color(255, 0, 0)
blue = Color(0, 0, 255)
 
magenta = red.add(blue)
print(magenta)
# Prints "Color with RGB = (255, 0, 255)"

#RENAME ADD
class Color: 
  def __add__(self, other):
    """
    Adds two RGB colors together
    Maximum value is 255
    """
    new_red = min(self.red + other.red, 255)
    new_green = min(self.green + other.green, 255)
    new_blue = min(self.blue + other.blue, 255)
 
    return Color(new_red, new_green, new_blue)

# Color with RGB: (255, 0, 255)
magenta = red + blue
 
# Color with RGB: (0, 255, 255)
cyan = green + blue
 
# Color with RGB: (255, 255, 0)
yellow = red + green
 
# Color with RGB: (255, 255, 255)
white = red + green + blue

###############################

#In script.py there are two classes defined, Atom and Molecule.

#Give Atom a .__add__(self, other) method that returns a Molecule with the two Atoms together in a list.
class Atom:
  def __init__(self, label):
    self.label = label
    
  def __add__(self, other):
    return Molecule([self, other])
    
class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
	    self.atoms = atoms
      
sodium = Atom("Na")
chlorine = Atom("Cl")

# salt = sodium + chlorine

##################### Dunder Methods II
class UserGroup:
  def __init__(self, users, permissions):
    self.user_list = users
    self.permissions = permissions
 
  def __iter__(self):
    return iter(self.user_list)
 
  def __len__(self):
    return len(self.user_list)
 
  def __contains__(self, user):
    return user in self.user_list

#__init__(), our constructor, which sets a list of users to the instance variable self.user_list and sets the group’s permissions when we create a new UserGroup.
#__iter__, the iterator, we use the iter() function to turn the list self.user_list into an iterator so we can use for user in user_group syntax. For more information on iterators, review Python’s documentation of Iterator Types.
#__len__, the length method, so when we call len(user_group) it will return the length of the underlying self.user_list list.
#__contains__, the check for containment, allows us to use user in user_group syntax to check if a User exists in the user_list we have.


class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers
  
  def __len__(self):
    return len(self.lawyers)

  def __contains__(self, lawyer):
    if lawyer in self.lawyers:
      return True

    
d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])

