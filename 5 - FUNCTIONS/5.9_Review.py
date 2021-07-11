# TripPlanner V1.0.

#We want to make sure to welcome our users to the application.
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)

#Next, we are going to generate messages for a user’s planned trip.

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in "+ origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  #nao pode printrar um inteiro direto -> str()
  #Ou usar o $
  print("It will take approximately $", estimated_time )

#calculate a rounded time value based on a decimal for our user’s trip.

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

trip_planner_welcome(" Renan e Skinny ")
estimate = estimated_time_rounded(2.43)
destination_setup(" Munique ", "Rome ", estimate, "Car")



