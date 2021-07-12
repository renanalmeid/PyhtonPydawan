#calculating which list of two inputs has the larger sum.
#We will iterate through each of the list and calculate the sums
#afterwards we will compare the two and return which one has a greater sum

def larger_sum(lst1, lst2):
  sum1 =0
  sum2 =0
  for index1 in lst1:
    sum1 += index1
  for index2 in lst2:
    sum2 += index2
  
  if sum1 >= sum2:
    return lst1
  else:
    return lst2


#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))