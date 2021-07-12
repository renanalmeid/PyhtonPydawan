#In this challenge, we will be using nested loops in order to raise a list of numbers to the power of a list of other numbers.
#What this means is that for every number in the first list, we will raise that number to the power of every number in the second list. 

def exponents(bases,powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base**power)
  return new_lst

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))