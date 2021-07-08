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
#func[start:end]
#start - onde começa 
#end onde o corte acontece mas para antes
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]

print(beginning)

middle = suitcase[2:4]
print(middle)

###Slicing Lists II
#func[:n]  -> pega os elementos até n
#fun[-n:] -> inverte ordem dos que pega 
#fun[:-n] --> todos exceto os n ultimos 
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below: 

last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)


###Counting a List
#method .count()
#.count retorna um valor
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below: 
jake_votes = votes.count("Jake")
print(jake_votes)

###Sorting List I
#method .sort


