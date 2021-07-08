#.count()
#.insert()
#.pop () remove specific index or from end
#range() create a sequence of integres
#len() comprimento 
#.sort()/sorted()  built-in function to sort a list

###Adding by Index Insert
#.insert() pode ser usado com indices negativos, expect 2 inputs
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]

front_display_list.insert(0, "Pineapple")
print(front_display_list)

###Removing by index: Pop
#sem indice:ultimo, com indice: indice
data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]

data_science_topics.pop()

data_science_topics.pop(3)
print(data_science_topics)

###Consecutive Lists: Range
#range cria um objeto e nao um vetor
#list() cria esse vetor

#cria obejto com 9 numb
number_list = range(9)

#printa vetor com esses numeros
print(list(number_list))

zero_to_seven = range(8)
print(list(zero_to_seven))

###The Power of Range!
#tem 2 inputs
# 3 inputs skips numbers (dita o steps que pula)
range_five_three = range(5, 15, 3)
range_diff_five = range (0, 40, 5)
print(range_diff_five)


###Length
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

long_list_len = len(long_list)
range_list = range(2, 3000, 100)
range_list_length = len(range_list)

print(long_list_len)
print(range_list_length)

###Slicing Lists I
