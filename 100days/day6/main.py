def ex_one(): 
    list = ["a", "b", "c", "d"]
    for char, index in enumerate(list):
        print(char, index)

ex_one()
# out:
# 0 a
# 1 b
# 2 c
# 3 d

p = "412tf"
z = "412tf"
print(id(p)) # 139988250435120
print(id(z)) # 139988250435120
print(id(p)) # 139988250435120

students = {"John": 88, "Sarah": 85, "Sam": 82, "Daniel": 90}
def dictionary_1(dictionary: dict[str, int])-> dict[str, int]:
    return { k + "!": v + 10 for (k, v) in zip(dictionary.keys(), dictionary.values()) }

print(dictionary_1(students))
# {'John!': 98, 'Sarah!': 95, 'Sam!': 92, 'Daniel!': 100}

def zipper(dict_):
    return zip(dict_.keys(), dict_.values())

def dictionary_2(dict_):
    return { k + "!": v + 10 for (k, v) in zipper(dict_) }

    
print(dictionary_2(students))

def while_loop(n: int)-> None:
    if n > 10:
        pass
    else:
        while n > 0:
            print(n)
            n -= 1

while_loop(11)
while_loop(9)


def while_2(): 
    n = 10
    while not n == 0:
        print(n)
        n -= 1

while_2()
