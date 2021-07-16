###########Get A Key

#We have provided a dictionary that maps the elements of astrology to the zodiac signs.
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

################Get an Invalid Key

#One way to avoid this error is to first check if the key exists in the dictionary:
#key_to_check = "Landmark 81"
 
#if key_to_check in building_heights:
#  print(building_heights["Landmark 81"])

#This will not throw an error, because key_to_check in building_heights will return False, and so we never try to access the key.


zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"],"energy": "Not a Zodiac element" }
print(zodiac_elements["energy"])


######## Try/Except to Get a Key
#We saw that we can avoid KeyErrors by checking if a key is in a dictionary first. Another method we could use is a try/except:


caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

#Use a try block to try to print the caffeine level of "matcha". If there is a KeyError, print "Unknown Caffeine Level".

#Above the try block, add "matcha" to the dictionary with a value of 30.

key_to_check = "matcha"
caffeine_level.update({"matcha": 30})
try:
  print(caffeine_level[key_to_check])
except KeyError:
  print("Unknown Caffeine Level")


  ##########Safely Get a Key
#We saw in the last exercise that we had to add a key:value pair to a dictionary in order to avoid a KeyError.
#This solution is not sustainable. We can’t predict every key a user may call and add all of those placeholder values to our dictionary!
#Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. If the key you are trying to .get() does not exist, it will return None by default:

#You can also specify a value to return if the key doesn’t exist.

# For example, we might want to return a building height of 0 if our desired building is not in the dictionary:


user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": "129384"}

#Use .get() to get the value of "teraCoder"‘s user ID, with 100000 as a default value if the user doesn’t exist. Store it in a variable called tc_id. Print tc_id to the console.

tc_id = user_ids.get('teraCoder', 100000)

print(tc_id)

stack_id = user_ids.get('superStrackSmash', 100000)
print(stack_id)

##############Delete a Key
#Sometimes we want to get a key and remove it from the dictionary. 
#We can use .pop() to do this. .pop() works to delete items from a dictionary, when you know the key value.

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

#In one line, add the corresponding value of the key "stamina grains" to the health_points variable and remove the item "stamina grains" from the dictionary. If the key does not exist, add 0 to health_points.

health_points += available_items.pop("stamina grains", 0)

health_points += available_items.pop("power stew", 0)

health_points += available_items.pop("mystic bread", 0)
print(available_items)
print(health_points)


#################Get All Keys
#Sometimes we want to operate on all of the keys in a dictionary. 
#We want to get a roster of the students in the class, without including their grades. We can do this with the built-in list() function:

#Dictionaries also have a .keys() method that returns a dict_keys object. 


#A dict_keys object is a view object, which provides a look at the current state of the dictionary, without the user being able to modify anything.
#. The dict_keys object returned by .keys() is a set of the keys in the dictionary. 
#You cannot add or remove elements from a dict_keys object, but it can be used in the place of a list for iteration:

#for student in test_scores.keys():
#  print(student)

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

#Create a variable called users and assign it to be a dict_keys object of all of the keys of the user_ids dictionary.
users = user_ids.keys()
print(users)
lessons = num_exercises.keys()
print(lessons)

############Get All Values
#Dictionaries have a .values() method that returns a dict_values object (just like a dict_keys object but for values!) with all of the values in the dictionary.
#There is no built-in function to get all of the values as a list, but if you really want to, you can use:
#list(test_scores.values())


num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0 
for index in list(num_exercises.values()): 
  total_exercises += index

print(total_exercises)

##############Get All Items
#You can get both the keys and the values with the .items() method. Like .keys() and .values(), it returns a dict_list object. Each element of the dict_list returned by .items() is a tuple consisting of:
#(key, value)


pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

#Use a for loop to iterate through the items of pct_women_in_occupation. For each key : value pair, print out a string that looks like:
for occupation, number in pct_women_in_occupation.items():
  print("Women make up "+ str(number) +" percent of "+occupation+ "s.")


