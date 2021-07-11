#You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

#the number of purchases for each hairstyle type in the last week.
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Each index in hairstyles corresponds to an associated index in prices and last_week.

###Prices and Cuts:
#1.Carly wants to be able to market her low prices
#First, let’s sum up all the prices of haircuts.
total_price = 0
for price in prices:
  total_price += price


average_price = total_price/len(prices)
print("Average Haircut Price: ", average_price)

#TOO expansive, cut each by 5 dol
new_prices =[new-5 for new in prices]
print(new_prices)



###Revenue:
#She first wants to know how much revenue was brought in last week.
total_revenue = 0

range_hairStyle = range(len(hairstyles))

for i in range_hairStyle: 
  total_revenue += prices[i]*last_week[i]

print("Total Revenue: ", total_revenue)
average_daily_revenue = total_revenue/7
print("Daily Average: ", average_daily_revenue)

#Use a list comprehension to create a list called cuts_under_30

cuts_under_30 = [
    hairstyles[i]
    for i in range(len(hairstyles))
    if new_prices[i] <30
]