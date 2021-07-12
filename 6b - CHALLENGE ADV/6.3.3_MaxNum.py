#This function will be used to find the maximum number in a list of numbers.
#This can be accomplished using the max() function in python, but as a challenge, we are going to manually implement this function.
def max_num(nums):
  max = nums[0]
  for index in nums:
    if index > max:
      max = index
  return max


#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))