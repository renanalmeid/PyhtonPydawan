# Let’s start our challenging problems with a function that creates a list of numbers up to 100 in 
# increments of 3 starting from a number that is passed to the function as an input parameter.

def every_three_nums(start):
  new_list =[]
  for index in range(start,101,3):
    new_list.append(index)
 
  return new_list
#Uncomment the line below when your function is done
print(every_three_nums(91))

######################
def every_three_nums(start):
  return list(range(start, 101, 3))