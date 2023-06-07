


# [<expression1> for <varname> in <iterable> if <expression2>]


list1 = [1, 2, 3]
list2 = [10, 20, 30]

list_comp1 = [x + y for x, y in zip(list1, list2)]
print(list_comp1) # [11, 22, 33]


filt_comp = [x for x in list1 if x % 2 == 0]
print(filt_comp) # [2]

l = range(10)
map_l = list(filter(lambda n: n < 25, map(lambda x: x**2, list1)))
print(map_l) # [1, 4, 9]


map_l_comp = [n**2 for n in list1 if n < 25]
print(map_l_comp) # [1, 4, 9]



