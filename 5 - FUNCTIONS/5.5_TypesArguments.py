#Positional arguments: arguments that can be called by their position in the function definition.

#Keyword arguments: arguments that can be called by their name.

#Default arguments: arguments that are given default values.

#TRIPACADEMY 

def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

trip_planner("Denmark","France","Germany")
trip_planner(first_destination="Iceland", final_destination="Germany", second_destination="India")

trip_planner("Brooklyn", "Queens")