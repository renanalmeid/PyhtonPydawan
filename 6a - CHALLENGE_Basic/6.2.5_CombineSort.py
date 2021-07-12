#function that combines two different lists together and then sorts them

def combine_sort(lst1, lst2):
  unsorted = lst1+lst2
  return sorted(unsorted)


#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))