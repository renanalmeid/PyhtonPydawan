#Let’s say we are working with two conveyor belts that contain items represented by a numerical ID

#If one conveyor belt contains more items than the other, then we need to return the ID of the last item on that belt

#lt. In the case where they have the same number of items, return the last item from the first conveyor belt.

def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))