#### 1- Check Name 

# Write your check_for_name function here:
def check_for_name (sentence,name):
  convert1 = sentence.upper()
  convert2 = name.upper()
  if convert2 in convert1:
    return True
  return False
# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
#print(check_for_name("My name is Samantha", "Jamie"))
# should print False

### 2- Every Other Letter
# Write your every_other_letter function here:
def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other
# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 

### 3 -Reverse
# Write your reverse_string function here:
def reverse_string(word):
  reversed_string = ""
  for i in range(len(word)-1, -1, -1):
   reversed_string += word[i]
  return reversed_string 
# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
#print(reverse_string("Hello world!"))
# should print !dlrow olleH
#print(reverse_string(""))
# should print


### 4 - Make Spoonerism
# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):

  return word2[0]+word1[1:] + " " + word1[0]+word2[1:]
# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a


### 5- Add Exclamation
# Write your add_exclamation function here:
def add_exclamation(word):
  while (len(word)<20):
    word += "!"
  return word
# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
#print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn


