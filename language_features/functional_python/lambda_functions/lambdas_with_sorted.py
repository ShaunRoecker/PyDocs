
# lambdas in sorting

lista = [1, 8, 4, 3, 6, 9, 10, 3, 7]

lista_sorted = sorted(lista)
print(lista_sorted) # [1, 3, 3, 4, 6, 7, 8, 9, 10]
print(lista) # [1, 8, 4, 3, 6, 9, 10, 3, 7]


l = ["c", "B", "A", "C", "D", "a"]

print(sorted(l))  # ['A', 'B', 'C', 'D', 'a', 'c']

print(ord("a")) # 97
print(ord("A")) # 65

print(sorted(l, key=lambda s: s.upper()))  # ['A', 'a', 'B', 'c', 'C', 'D']

# the function used in the key parameter takes in the element
# in the iterable, for lists it is the element itself, and
# for dictionaries, it is a tuple of the (key, value)

d = {"def": 300, "abc": 200, "ghi": 100}

print(sorted(d)) # ['abc', 'def', 'ghi']

sorted(d, key=lambda e: d[e]) # ['abc', 'def', 'ghi']

# sort a dictionary on VALUES, returning a dictionary
print(dict(sorted(d.items(), key=lambda x: x[1]))) # {'ghi': 100, 'abc': 200, 'def': 300}

# the x[1] here is referring to the tuple that makes up each key-value pair 
# in a dictionary   ("def", 300) -->  x[1] --> 300

# sort a dictionary on KEYS, returning a dictionary
print(dict(sorted(d.items(), key=lambda x: x[0]))) # {'abc': 200, 'def': 300, 'ghi': 100}

# the x[1] here is referring to the tuple that makes up each key-value pair 
# in a dictionary   ("def", 300) -->  x[0] --> "def"

print(d.items()) # dict_items([('def', 300), ('abc', 200), ('ghi', 100)])



l = ["Chapman", "Cleese", "Gillian", "Idle", "Jones", "Palin"]

# sort a list of strings on the last character of each string
print(sorted(l, key=lambda x: x[-1])) 
# ['Cleese', 'Idle', 'Chapman', 'Gillian', 'Palin', 'Jones']

# can use the "reverse" parameter to sort in descending order
print(sorted(l, key=lambda x: x[-1], reverse=True)) 
# ['Jones', 'Chapman', 'Gillian', 'Palin', 'Cleese', 'Idle']


import random

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

randomized_list = sorted(l, key=lambda x: random.random())
print(randomized_list)
# [9, 1, 2, 8, 3, 4, 10, 7, 5, 6]

