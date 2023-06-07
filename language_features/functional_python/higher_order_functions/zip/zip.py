

l1 = [1, 2, 3, 4]
l2 = [10, 20, 30, 40]
l3 = [100, 200, 300, 400]
l4 = "python"


# zip returns an iterable
zipped1 = zip(l1, l2)
print(zipped1)  # <zip object at 0x7fe3335fe7c0>

# to get a list back
zipped_list = list(zip(l1, l2))
print(zipped_list) # [(1, 10), (2, 20), (3, 30), (4, 40)]

zipped_list3 = list(zip(l1, l2, l3))
print(zipped_list3) # [(1, 10, 100), (2, 20, 200), (3, 30, 300), (4, 40, 400)]


def add3(a, b, c):
    return a + b + c


lst_tuple = [x for x in zip(*[iter(l1)]*2)]
print(lst_tuple) # [(1, 2), (3, 4)]


list_tuple2 = list(zip(l1, l2, l4))
print(list_tuple2) # [(1, 10, 'p'), (2, 20, 'y'), (3, 30, 't'), (4, 40, 'h')]

l1 = "abcd"

zip_with_index1 = list(zip(l1, range(len(l1))))
print(zip_with_index1) # [('a', 0), ('b', 1), ('c', 2), ('d', 3)]

zip_with_index2 = list(zip(range(len(l1)), l1))
print(zip_with_index2) # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]



