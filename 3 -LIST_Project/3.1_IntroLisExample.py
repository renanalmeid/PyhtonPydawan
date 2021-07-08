################ Example_1 Method
#method .append() inserts an element on the last position
append_example = [ 'This', 'is', 'an', 'example']
append_example.append('list')
 
print(append_example)

#.remove tira o ultimo

example_list = [1, 2, 3, 4]

#Using Append
example_list.append(0)
print(example_list)

#Using Remove
example_list.remove(0)
print(example_list)

################### .remove tira elementos de algo 
##.remove nao trabalha com posição 


################### Lista 2D
class_name_test =[["Jenny",90],["Alexus",85.5],["Sam",83],["Ellie",101.5]]

print(class_name_test)

sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)


#ex2
#negative index a partir de -1 
#positive index a partir de 0 
incoming_class = [["Kenny", "American", 9], ["Tanya", "Russian", 9], ["Madison", "Indian", 7]]
incoming_class[2][2] = 8
incoming_class[-3][-3] = "Ken"
print(incoming_class)

#.reshape redimensiona o vetor para ourtra dimensao
#o proprio usuario coloca a propria dimensao




