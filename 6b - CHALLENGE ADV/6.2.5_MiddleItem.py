#we are going to create a function that finds the middle item from a list of values. 
#This will be different depending on whether there are an odd or even number of values.
#In the case of an odd number of elements, we want this function to return the exact middle value
# If there is an even number of elements, it returns the average of the middle two elements. 
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]


#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))