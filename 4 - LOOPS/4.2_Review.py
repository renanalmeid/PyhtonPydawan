# Create a list called single_digits that consists of the numbers 0-9
single_digits = list(range(10))
#Create a for loop that goes through single_digits and prints out each one.
#Create a list called squares. Assign it to be an empty 
squares =[]
for number in single_digits:

#append the squared value of each element of single_digits to the list squares.

  number_squared = number**2
  squares.append(number_squared)
  print(number)

print(squares)

#Create the list cubes using a list comprehension on the single_digits list.
# Each element of cubes should be an element of single_digits taken to the third power.
cubes =[number_cube**3 for number_cube in single_digits ]
print(cubes)