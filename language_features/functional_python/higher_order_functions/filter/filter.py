

l = [0, 1, 2, 3, 4]

filt1 = list(filter(None, l))
print(filt1)


def is_even(n: int)-> bool:
    return n % 2 == 0


filt_even = list(filter(is_even, l)) # [1, 2, 3, 4]
print(filt_even) # [0, 2, 4]

filt_even2 = list(filter(lambda x: x % 2 == 0, l))
print(filt_even2) # [0, 2, 4]


x = range(25)
result = list(filter(lambda x: x % 3 == 0, range(25)))
print(result) # [0, 3, 6, 9, 12, 15, 18, 21, 24]


# get all truthy values with filter
values = [1, 0, 4, "a", "", None, True, False]
truthy = list(filter(None, values))
print(truthy) # [1, 4, 'a', True]

