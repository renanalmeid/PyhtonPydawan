#It’s time to re-create a famous movie scene through code.
#Our function is going to concatenate strings together in order to replace James Bond’s name with whatever name we want
#The input to our function will be two strings, one for a first name and another for a last name. 

def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name

# Uncomment these function calls to test your introduction function:
#print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

