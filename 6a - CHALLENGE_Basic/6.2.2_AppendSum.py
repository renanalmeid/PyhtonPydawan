#function that calculates the sum of the last two elements of a list and appends it to the end.

# it will repeat this process two more times and return the resulting list.

def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst
  

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))