#############Introduction to Dictionary
#A dictionary is an unordered set of key: value pairs.

#It provides us with a way to map pieces of data to each other so that we can quickly find values that are associated with one another.

#A dictionary begins and ends with curly braces { and }.
#Each item consists of a key ("avocado toast") and a value (6).
#Each key: value pair is separated by a comma.

#Suppose we have a dictionary of temperature sensors in the house and what temperatures they read. 
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)


####### Make a Dictionary
#the keys can be numbers as well.
#Values can be of any type. We can use a string, a number, a list, or even another dictionary as the value associated with a key!
#We can also mix and match key and value types.


translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

########### Invalid Keys
#We can have a list or a dictionary as a value of an item in a dictionary, but we cannot use these data types as keys of the dictionar

#The word “unhashable” in this context means that this ‘list’ is an object that can be changed.

#The word “unhashable” in this context means that this ‘list’ is an object that can be changed.
#Dictionaries in Python rely on each key having a hash value, a specific identifier for the key
#f the key can change, that hash value would not be reliable. So the keys must always be unchangeable, hashable data types, like numbers or strings.

children = {"von Trapp":["Johannes", "Rosmarie", "Eleonore"], "Corleone":["Sonny", "Fredo", "Michael"]}

###### Empty Dictionary
#A dictionary doesn’t have to contain anything. Sometimes we need to create an empty dictionary when we plan to fill it later based on some other input.

my_empty_dictionary ={}

#########Add a Key 
#To add a single key: value pair to a dictionary, we can use the syntax:
#dictionary[key] = value


#For example, if we had our menu dictionary from the first exercise:
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
#And we wanted to add a new item, "cheesecake" for 8 dollars, we could use:
menu["cheesecake"] = 8

#Now, menu looks like:
#{"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2, "cheesecake": 8}

animals_in_zoo ={}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)

##########Add multiple keys
#If we wanted to add multiple key : value pairs to a dictionary at once, we can use the .update() method.

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

##############List Comprehensions to Dictionaries
#Python allows you to create a dictionary using a list comprehension,

#names = ['Jenny', 'Alexus', 'Sam', 'Grace']
#heights = [61, 70, 67, 64]
#students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

#Remember that zip() combines two lists into a zipped list of pairs.
#1 Takes a pair from the zipped list of pairs from names and heights
#2 Names the elements in the pair key (the one originally from the names list) and value (the one originally from the heights list)
#3 Creates a key : value item in the students dictionary
#Repeats steps 1-3 for the entire list of pairs


#You have two lists, representing some drinks sold at a coffee shop and the milligrams of caffeine in each
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

#First, create a variable called zipped_drinks that is a zipped list of pairs between the drinks list and the caffeine list.
zipped_drinks = zip(drinks, caffeine)

#Create a dictionary called drinks_to_caffeine by using a list comprehension that goes through the zipped_drinks list and turns each pair into a key:value item.

drinks_to_caffeine = {key:value for key, value in zipped_drinks}
