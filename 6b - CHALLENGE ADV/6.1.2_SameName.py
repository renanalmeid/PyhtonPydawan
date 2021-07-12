# We need to write a program that checks different names and determines if they are equal.
# We need to accept two strings and compare them.

def same_name(your_name, my_name):
  if (your_name == my_name):
    return True 
  return False

# Uncomment these function calls to test your same_name function:
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False