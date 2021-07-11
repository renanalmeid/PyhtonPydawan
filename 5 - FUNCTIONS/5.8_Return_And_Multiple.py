#When there is a result from a function that is stored in a variable, it is called a returned function value.

#Example1_Return

current_budget = 3500.75
shirt_expense = 9 


def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

#Our function will be taking in a budget value as well as the expense we want to subtract.

#We will want our function to return the budget minus the expense our travelers are incurring.

def deduct_expense(budget, expense):
  return budget-expense

#Looks like the most common expense our travelers are incurring is a t-shirt purchase.


new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)

################ Second example
#e want to create a small function to output the top places to visit in Italy. 

def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third 

#top_tourist_locations_italy() 

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)