toppings = ["pepperoni",  "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices =[2,6,1,3,2,7,2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
num_pizzas = len(toppings)
print("We sell ", num_pizzas, " different kinds of pizza!")

pizza_and_prices = [[2,"pepperoni"],  [6,"pineapple"], [1,"cheese"], [3,"sausage"], [2,"olives"], [7,"anchovies"], [2,"mushrooms"]]

sorted_pizza = sorted (pizza_and_prices)

print(sorted_pizza)

cheapest_pizza = sorted_pizza[0]
priciest_pizza = sorted_pizza[-1]
sorted_pizza.pop()

sorted_pizza.insert(5, [2.5, "peppers"])
three_cheapest = sorted_pizza[0:3]

print(three_cheapest)