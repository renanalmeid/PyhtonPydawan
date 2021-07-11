#You are a physics teacher preparing for the upcoming semester. 
#You want to provide your students with some functions that will help them calculate some fundamental physical properties.

###Convert Fahrenheit to Celsius
def f_to_c(f_temp):
  c_temp = (f_temp-32)*5/9
  return c_temp

def c_to_f(c_temp):
  f_temp = c_temp*(9/5)+32
  return f_temp

f100_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)

###UseForce
train_mass = 22680
train_acceleration = 10

def get_force(mass, acceleration):
  return mass*acceleration

train_force = get_force(train_mass,train_acceleration)

print("The GE train supplies "+str(train_force)+ " Newtons of force.")

## calculating Energy
bomb_mass = 1
def get_energy(mass, c=3*10**8):
  return mass*c

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies "+ str(bomb_energy) + " Joules")



###### Do the Work
train_distance = 100
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  work = force*distance
  return work

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance)+ " meters.")





