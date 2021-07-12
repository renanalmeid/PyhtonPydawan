# testing if a number falls within a certain range

# We will accept three parameters where the 
#first parameter is the number we are testing, 
#the second parameter is the lower bound and 
#the third parameter is the upper bound of our range.

def in_range(num, lower, upper):
 if num >= lower and num <= upper:
   return True
 else:
   return False



# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False


#############
def in_range(num, lower, upper):
  if(num >= lower and num <= upper):
    return True
  return False