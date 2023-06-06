# Docstrings
from typing import List, Tuple


def my_func(i: int, xs: List[str])-> List[Tuple[int, str]]:
    """
    a function that takes an int and a list of strings,
    creates a tuple2 from that int and each string in the list,
    and returns a list of tuples
    """
    return [(s, i) for s in xs]


print(help(my_func))
print("\n\n")
print(my_func.__doc__) # <-- displays the docstring of the method
print(my_func.__annotations__)
# {'i': <class 'int'>, 'xs': typing.List[str], 'return': typing.List[typing.Tuple[int, str]]}


alist = ["a", "b", "c", "d"]
print(my_func(10, alist)) # [('a', 10), ('b', 10), ('c', 10), ('d', 10)]


