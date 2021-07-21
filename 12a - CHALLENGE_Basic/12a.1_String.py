#1. Count Letters
#For the first code challenge, we are going to count the number of unique letters in a string. This means that when we are looking at the word, any new letters should be counted and any duplicates should not be counted. There are a few ways to solve this, but we can use the provided alphabet string to ensure that duplicates are not counted. Here is what we need to do:


#### Test1 - Count Letters
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:

def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word: 
      uniques += 1
  return uniques
# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4


#### Test 2 - Count X
# Write your count_char_x function here:
def count_char_x(word, x):
  counter = 0
  for letter in word:
    if letter == x:
      counter += 1
  return counter

# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

#### 3 - Count Multi X

# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  parameter = word.split(x)
  return (len(parameter)-1)
# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

#### 4 - Substring Between
# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  start_ind = word.find(start)
  end_ind = word.find(end)
  if start_ind > -1 and end_ind > -1:
    return (word[start_ind+1:end_ind])
 
  return word
# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

#### 5- X Length
# Write your x_length_words function here:
def x_length_words(sentence, x):
  words = sentence.split(" ")
  for word in words: 
    if len(word) < x:
      return False
  return True
# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
