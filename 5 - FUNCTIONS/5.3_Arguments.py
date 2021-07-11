#Function parameters allow our function to accept data as an input value

#The parameter is the name defined in the parenthesis of the function and can be used in the function body.
#The argument is the data that is passed in when we call the function and assigned to the parameter name

#We want to create a program that allows our users to generate the directions for their upcoming trip!

# Your code below:

def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to "+ location)

generate_trip_instructions("Grand Central Station")