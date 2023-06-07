from typing import List
from functools import reduce



l = [5, 8, 6, 10, 9, 0]

max_value = lambda x, y: x if x > y else y

def max_sequence(seq):
    result = seq[0]
    for i in seq[1:]:
        result = max_value(result, i)
    return result


def _reduce(fn, sequence):
    result = sequence[0]
    for i in sequence[1:]:
        result = fn(result, i)
    return result

add = lambda x, y: x + y

reduced = _reduce(add, l)
print(reduced) # 38



reduced2 = reduce(max_value, l)
print(reduced2) # 10


reduced_max = reduce(lambda a, b: a if a > b else b, l)
print(reduced_max)



reduce_to_any = reduce(lambda a, b: bool(a) or bool(b), l)
print(reduce_to_any) # True

reduce_to_all = reduce(lambda a, b: bool(a) and bool(b), l)
print(reduce_to_all) # False


#factorial
factorial = lambda n : reduce(lambda a, b: a * b, range(1, n+1))
print(factorial(5)) # 120



zipped = list(zip(range(len(l)), l))
print(zipped) # [(0, 5), (1, 8), (2, 6), (3, 10), (4, 9)]

tuple_reduce = reduce(lambda a, b: (a[0] + b[0], a[1] + b[1]), zipped)
print(tuple_reduce) # (15, 38)



