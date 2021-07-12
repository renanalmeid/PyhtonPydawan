# We have a conveyor belt of items where each item is represented by a different number. 
#We want to know, out of two items, which one shows up more on our belt

def more_frequent_item(lst, item1, item2):
  new_lst1 = lst.count(item1)
  new_lst2 = lst.count(item2)
  if new_lst1 >= new_lst2:
    return item1
  else:
    return item2

#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))