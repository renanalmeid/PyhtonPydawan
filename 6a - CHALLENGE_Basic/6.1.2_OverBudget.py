# Let’s say we are trying to save some money and we are watching our budge

#We need to make sure that the result of our spending is less than the total amount we have allocated for each of the categories. 

def over_budget (budget, food_bill, electricity_bill, internet_bill, rent):
  sum_bills = food_bill+electricity_bill+internet_bill+rent
  if sum_bills> budget:
    return True
  else:
    return False

# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True



####################
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if (budget < food_bill + electricity_bill + internet_bill + rent):
    return True
  else:
    return False