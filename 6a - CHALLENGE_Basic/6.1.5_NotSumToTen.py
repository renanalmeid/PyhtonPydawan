# We are going to check if the summation of two inputs does not equal ten

def not_sum_to_ten(num1,num2):
  sum = num1+num2

  if sum != 10:
    return True
  else:
    return False

  
# Uncomment these function calls to test your not_sum_to_ten function:
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5,5))
# should print False

#############
def not_sum_to_ten(num1, num2):
  if (num1 + num2 != 10):
    return True
  else:
    return False