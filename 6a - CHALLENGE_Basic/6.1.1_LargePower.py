#We are going to create a method that tests whether the result of taking the power of one number to another number provides an answer which is greater than 5000

def large_power(base, exponent):
  LP = base**exponent
  if LP > 5000:
    return True
  else:
    return False


print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False