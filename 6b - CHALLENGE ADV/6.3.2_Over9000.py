#We are constructing a device that is able to measure the power level of our coding abilities and according to the device, it will be impossible for our power levels to be over 9000.
# Because of this, as we iterate through a list of power values we will count up each of the numbers until our sum reaches a value greater than 9000.
#Once this happens, we should stop adding the numbers and return the value where we stopped. 
def over_nine_thousand(lst):
  track_sum = 0
  for index in lst:
    track_sum += index
    if track_sum > 9000:
      break
    else:
      continue
  return track_sum


#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))