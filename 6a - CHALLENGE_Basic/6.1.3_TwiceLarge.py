#Determine if one number is twice as large as another number. To do this, we will compare the first number with two times the second number.

def twice_as_large(num1, num2):
  if(num1>2*num2):
    return True
  else:
    return False

# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True


#######################
def twice_as_large(num1, num2):
  if num1 > 2 * num2:
    return True
  else:
    return False