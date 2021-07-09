#The zip() function allows us to quickly combine associated
#data-sets without needing to rely on multi-dimensional lists.

name = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 65]
names_and_heights = zip(names, heights)

print(names_and_heights)
#Would output:
#<zip object at 0x7f1631e86b48>

converted_list = list(names_and_heights)

print(converted_list)



#############Exemplo
owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

names_and_dogs_names = zip(owners, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)