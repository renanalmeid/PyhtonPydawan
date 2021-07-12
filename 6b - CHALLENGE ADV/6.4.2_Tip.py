# Let’s say we are going to a restaurant and we decide to leave a tip. 
# We can create a function to easily calculate the amount to tip based on the total cost of the food and a percentage. 
# This function will accept both of those values as inputs and return the amount of money to tip. 

def tip(total, percentage):
  return (total*percentage)/100
  
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0