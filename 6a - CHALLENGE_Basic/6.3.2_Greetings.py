#You are invited to a social gathering, but you are tired of greeting everyone there.

def add_greetings(names):
  
  empty_greeting =[print("Hello,  " + str(index)) for index in names]


#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))


def add_greetings(names):
  new_list = []
  for name in names:
    new_list.append("Hello, " + name)
  return new_list