# we need to find the indices in two equally sized lists where the numbers match.
# We will be iterating through both of them at the same time and comparing the values
# if the numbers are equal, then we record the index

def same_values(lst1, lst2):
  index_store=[]
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      index_store.append(index)
  return index_store
   

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))