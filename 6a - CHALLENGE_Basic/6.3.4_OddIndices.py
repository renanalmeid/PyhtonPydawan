#This next function will give us the values from a list at every odd index. 

#We will need to accept a list of numbers as an input parameter and loop through the odd indices instead of the elements.

def odd_indices(lst):
  new_lst = []
  for index in range(len(lst)):
    if (index % 2 != 0):
     new_lst.append(lst[index])
  return new_lst

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))