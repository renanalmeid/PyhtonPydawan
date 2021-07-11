### Introduction

# General function 'for'

#for <temporary variable> in <collection>:
#  <action>

  # has variable temporary 
board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
  print(game)

for sport in sport_games: 
  print(sport)

### RANGE
# temp serve para fazer o trackking 
# Esse codigo abaixo printa a frase 5x
promise = "I will finish the python loops module!"

for i in range(5):
  print(promise)

#
promise = "I will finish the python loops module!"

for i in range(5):
  print(promise, str(i+1))

  #for <temporary variable> in range(<length>): 
  #<action>

### While 
#while <conditional statement>:
#  <action>


#Example1
count = 0
while count <= 3:
  # Loop Body
  print(count)
  count += 1

#Elegant loops (separa a linha por ponto e virgula)
count = 0
while count <= 3: print(count); count += 1

#CTRL + ;  comenta tudo 
#Example2
#Count down 10 ->0 -> print out "We have liftoff!"
countdown = 10 

while countdown >= 0:
  print(countdown)
  countdown -=1

print("We have liftoff!")

###While: lists
python_topics = ["variables", "control flow", "loops", "modules", "classes"]
#First, we will need a variable to represent the length of the list.
length =  len(python_topics)
#we will require a variable to compare to our length variable to make sure we are able to implement a condition that eventually allows the loop to stop.
index = 0

#while

while index < length:
  print("I am learning about " + python_topics[index])
  index +=1


### INFINITE LOOPS
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  # Pega vetor B e adiciona o estudante I do A no B através do append
  students_period_B.append(student)
  #printa quais estudantes foram adicionados em B 
  print(student)

#printa o B novo
print(students_period_B)


#### Loop control: break
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want: 
    print("They have the dog I want!")
    break

### Loop control: continue
#Loop through the ages list.
#  If an entry is less than 21, skip it and move to the next entry.
#  Otherwise, print() the age
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
  if i<21:
    continue
  print(i)


  ### NestedLoops
project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]

# Loop through each sublist
for team in project_teams:
  print(team)
  # Loop elements in each sublist
  for student in team:
    print(student)


#Example: storing numbers in a variable 
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for element in location:
    scoops_sold += element
    
print(scoops_sold)


### List Comprehensions: Intro
#elegant way to write while/for


#Example0
numbers = [2, -1, 79, 33, -45]
doubled = []
 
for number in numbers:
  doubled.append(number * 2)
 
print(doubled)

#RewriteExample0
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)

#new_list = [<expression> for <element> in <collection>]
#add 10 em cada for
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades =[num+10 for num in grades]
print(scaled_grades)

### List Comprehensions: Conditionals 

#Example0 
numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []
 
for num in numbers:
  if num < 0: 
    only_negative_doubled.append(num * 2)
 
print(only_negative_doubled) 

#RewriteExample0
numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled)

#da pra usar IF/ELSE
#For example, let’s say we wanted to double every negative number but triple all positive numbers. 
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers ]
print(doubled)

# Example1
#Using a list comprehension, 
# create a new list called can_ride_coaster that has every element 
# from heights that is greater than 161.
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [VAR  for VAR in heights if VAR > 161]
print(can_ride_coaster)
