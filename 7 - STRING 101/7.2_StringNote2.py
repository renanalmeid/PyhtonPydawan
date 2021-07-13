#### Methods

#.lower()
#.upper()
#.title() returns the string in title case, which means the first letter of each word is capitalized.
#.split() is performed on a string, takes one argument, 
# and returns a list of substrings found between the given argument
#If you do not provide an argument for .split() it will default to splitting at spaces.


#Create another list called author_last_names that only contains
#  the last names of the poets in the provided string.

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')

print(author_names)

author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
  
print(author_last_names)

#### We can also split strings using escape sequences
#\n Newline will allow us to split a multi-line string by line break
#\t Horizontal Tab will allow us to split a string by tabs.


#.join() is essentially the opposite of .split(), it joins a list of strings 
# together with a given delimiter.

#'delimiter'.join(list_you_want_to_join)

#but now the argument is the list
#.join() acts on is the delimiter you want to join with, therefore the list you want to join has to be the argument.

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)
print(reapers_line_one)

# example 2
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full ='\n'.join(winter_trees_lines)
print(winter_trees_full)


###### method .strip()
#Stripping a string removes all whitespace characters from the beginning and end. 
#with a character argument, which will strip that character from either end of the string.

# Exemplo: pega espaço de cada lugar e printa em uma str
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []

for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())
  
love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)


###### Replace

#.replace(). Replace takes two arguments and 
# replaces all instances of the first argument in a string with the second argument.


###### .find()
#takes a string as an argument and searching the string it was run on for that string. 
# It then returns the first index value where that string is located.
god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find('disown')

print(disown_placement)

#return 20


########### .format()
#handy string method for including variables in strings.
#takes variables as an argument and includes them in the string that it is run on.
#You include {} marks as placeholders for where those variables will be imported.

def poem_title_card(title, poet):
  poem_desc = "The poem \"{}\" is written by {}.".format(title, poet)
  return poem_desc

#you had to make sure that your variables appeared as arguments in the same order that you wanted them to appear 
#in the string, which just added unnecessary complications when writing code.

def favorite_song_statement(song, artist):
    return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)

#Example 2
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
  return poem_desc

author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(publishing_date, author, title, original_work)

print(my_beard_description)

