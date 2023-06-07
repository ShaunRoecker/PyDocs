

list1 = [2, 3, 4]

mapped_list1 = list(map(lambda x: x**2, list1))
print(mapped_list1) # [4, 9, 16]


list1 = [1, 2, 3]
list2 = [10, 20, 30]

map_list2 = list(map(lambda x, y: x + y, list1, list2))
print(map_list2) # [11, 22, 33]




def factorial(n: int)-> int: 
    return 1 if n < 2 else n * factorial(n-1)


results = list(map(factorial, range(6)))
print(results)


l1 = [1, 2, 3, 4]
l2 = [10, 20, 30, 40]
l3 = [100, 200, 300, 400]

result = list(map(lambda x, y, z: x + y + z, l1, l2, l3))
print(result) # [111, 222, 333, 444]





