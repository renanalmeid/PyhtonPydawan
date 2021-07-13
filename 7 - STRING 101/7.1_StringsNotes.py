#index para acessar string
#Write a function called account_generator() that takes two inputs, first_name and last_name 
#and concatenates the first three letters of each and then returns the new account name.

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  new_account = first_name[:3] + last_name[:3]
  return new_account

new_account = account_generator(first_name, last_name)


### REESCREVENDO STRING USANDO SLICING

first_name = "Bob"
last_name = "Daily"

#first_name[0] = "R"

fixed_first_name = "R" +first_name[1:]

print(fixed_first_name)

######### SCAPE CHRACTER

#favorite_fruit_conversation = "He said, "blueberries are my favorite!""
favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""


### String and Conditionals Pt1
#Write a function called letter_check that takes two inputs, word and letter.
#This function should return True if the word contains the letter and False if it does not.


def letter_check(word,letter):
  for char in word: 
    if char == letter:
      return True
  return False


skinny_sonso = letter_check("igor","g")

print(skinny_sonso)

### Pt2

#"in" checks if one string is part of another string.
#is a boolean expression

#Write a function called contains that takes two arguments, 
#big_string and little_string and returns True if big_string contains little_string.
def contains(big_string,little_string):
  if little_string in big_string:
    return True
  return False

#then returns a list with all of the letters they have in common.

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common


##To shift the letters right, at each letter the for
#  loop should add the previous letter to the string password.
def username_generator(first_name, last_name):
  username = first_name[:3]+last_name[:4]
  return username

def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password