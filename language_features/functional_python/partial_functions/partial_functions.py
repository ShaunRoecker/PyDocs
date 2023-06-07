from typing import Callable, TypeVar
from functools import partial




T = TypeVar("T")


identity: Callable[[T], T] = lambda x: x



add: Callable[[int, int], int] = lambda x, y: x + y

add2: Callable[[int], int] = lambda x: add(2, x)



print(add(2, 3))
print(add2(3))

print(identity(42))  # 42


def my_func(a, b, c):
    print(a, b, c)


def fn(b, c):
    return my_func(10, b, c)



f = partial(my_func, 10)


def my_func(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)

def f(b, *args, k2, **kwargs):
    return my_func(10, b, *args, k1="a", k2=k2, **kwargs)


f = partial(my_func, 10, k1="a")


def pow(base, exponent):
    return base ** exponent


square = partial(pow, exponent=2)
cube = partial(pow, exponent=3)


print(square(5)) # 25



