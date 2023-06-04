from typing import List, Tuple, Callable



# Default Values

def my_func(a: int, b: int = 5, c: int = 10)-> None:
    print(f"a: {a}, b: {b}, c: {c}")

my_func(1)          # a: 1, b: 5, c: 10
my_func(1, 7)       # a: 1, b: 7, c: 10


# Unpacking Packed Values:

# Unpacking is the act of splitting packed values into 
#   individual variables contained in a list or tuple

a, b, c = [10, 20, 30]
d, e, f = (40, 50, 60)
g, h, i = "ghi"
print(a, b, c, d, e, f, g, h, i)  # 10 20 30 40 50 60 g h i


print("\nswapping")
a = "a"
b = "b"
print(f"a: {a}") # a: a
print(f"b: {b}") # b: b


# to swap a, b without a temp variable...
a, b = b, a

print(f"a: {a}") # a: b
print(f"b: {b}") # b: a


# Unpacking Dictionaries and Sets doen't work the 
# same because they are not ordered, and there's
# no guarantee what element you will get


a, b, *c = [1, 2, 3, 4]
print(a, b, c)  # 1, 2, [3, 4]



# Extended Unpacking

l = [1, 2, 3, 4, 5, 6]
a, *b = l

print(f"a: {a}")  # a: 1
print(f"b: {b}")  # b: [2, 3, 4, 5, 6]

a, *b, c = [1, 2, 3, 4, 5, 6]
print(a, b, c) # 1 [2, 3, 4, 5] 6


# Merging Dictionaries
d1 = {"a": 1, "b": 1}
d2 = {"a": 1, "c": 1}
d3 = {"b": 1, "d": 1, "a": 2}

d = { **d1, **d2, **d3 }
print(d) # {'a': 2, 'b': 1, 'c': 1, 'd': 1}
# Note** it's not the sum of the values when using this technique,
# it updates a value if there are multiple in the dict with
# the last one.


new_dict = {"a1": 1, "b1": 1, **d3}
print(new_dict) # {'a1': 1, 'b1': 1, 'b': 1, 'd': 1, 'a': 2}


# Nested Unpacking

l = [1, 2, [3, 4]]

a, b, c = l
print(a, b, c) #1 2 [3, 4]

a, b, (c, d) = [1, 2, [3, 4]]
print(a, b, c, d) # 1 2 3 4

a, *b, (c, d, e) = [1, 2, 3, "XYZ"]
print(a, b, c, d, e) 
# a: 1
# b: [2, 3]  
# c: X 
# d: Y
# e: Z


a, *b, (c, *d) = [1, 2, 3, "python"]
print(a, b, c, d) 
# a: 1
# b: [2, 3] 
# c: p
# d: ['y', 't', 'h', 'o', 'n']


l = [1, 2, 3, 4, 5, 6]

a = l[0]
b = l[1:]
print(a)
print(b)


s = "python"
a, *b = s
print(a) # p
print(b)  # ['y', 't', 'h', 'o', 'n']  note: this style of unpacking always results in a list


*v, f = s

print(v) # ['p', 'y', 't', 'h', 'o']
print(f) # n

print(''.join(v)) # pytho


s = "abc"
l1 = [1, 2, 3]
flattened1 = [*s, *l1]
print(flattened1)

flattened = [*l1, *list(map(lambda x: x+ 1, l1))]
print(flattened) # [1, 2, 3, 2, 3, 4]

s = {'d', 12, 3, -99}
xs = list(s)
print(xs) # [3, 'd', 12, -99]
# can also
*c, = s
print(c) # [3, 'd', 12, -99]


s = {'d', 12, 3, -99}
v = {'c', 12, 2, -98}
t = {'e', 12, 5, -97}
y = {'c', 12, 6, -98}


sv = {*s, *v}
print(sv) # {2, 3, 'c', 12, 'd', -99, -98}

sv2 = s.union(v)
print(sv2) # {2, 3, 'c', 12, 'd', -99, -98}



set1 = s.union(v, t, y)
print(set1) # {'c', 2, 3, 5, 6, 12, 'e', 'd', -99, -98, -97}

set2 = {*s, *v, *t, * y}
print(set2) # {'c', 2, 3, 5, 6, 12, 'e', 'd', -99, -98, -97}


#dictionaries
d1 = {"key1": 1, "key2": 2}
d2 = {"key2": 3, "key4": 4}

dk = {*d1, *d2}
print(dk) # {'key2', 'key4', 'key1'}

dkv = {**d1, **d2}
print(dkv) # {'key1': 1, 'key2': 3, 'key4': 4}



