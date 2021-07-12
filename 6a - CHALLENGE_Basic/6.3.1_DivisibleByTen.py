#Let’s start our code challenges with a function that counts how many numbers are divisible by ten from a list of numbers. 

#This function will accept a list of numbers as an input parameter and use a loop to check each of the numbers in the list. 

#. Every time a number is divisible by 10, a counter will be incremented and the final count will be returned.

def divisible_by_ten(nums):
  counter = 0
  for index in nums:
    if (index % 10 == 0):
      counter +=1
  return counter  

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))