# If a variable lives outside of any function it can be accessed anywhere in the file.


#Example

#Our users want to be able to save a list of their favorite places in our travel application


favorite_locations = "Paris, Norway, Iceland"
# This function will print a hardcoded count of how many locations we have.
def print_count_locations():

    print("There are 3 locations")
    
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations()