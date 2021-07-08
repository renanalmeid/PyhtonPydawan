  
def shipping_cost_ground(weight):
  
  #Ground shipping 
   
  if weight <= 2:
    price_pp_gs = 1.50

  elif weight <= 6:
    price_pp_gs = 3.00

  elif weight <= 10:
    price_pp_gs = 4.00

  else:
    price_pp_gs = 4.75
   
  return 20 + (price_pp_gs*weight)

print(shipping_cost_ground(0))

  #Ground shipping premium

cost_ground_premium = 125.00

print ("Ground Shipping Premium $",cost_ground_premium)


  #Drone shipping

def shipping_cost_drone(weight):
  if weight <= 2:
    price_pp_drone = 4.50

  elif weight <= 6:
    price_pp_drone = 9.00

  elif weight <= 10:
    price_pp_drone = 12.00

  else:
    price_pp_drone = 14.25

  return (price_pp_drone*weight)
print (shipping_cost_drone(1.5))

def print_cheapest_shipping_method(weight):
  
  ground = shipping_cost_ground(weight)
  premium = cost_ground_premium
  drone = shipping_cost_drone(weight)

  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground

  elif premium < ground and premium < drone: 
    method = "premium ground"
    cost = premium
  else:
    method = "drone"
    cost = ground

  print ("The cheapest option availabe is $%.2f with %s shipping." %(cost, method))

print_cheapest_shipping_method(9)
print_cheapest_shipping_method(41.5)