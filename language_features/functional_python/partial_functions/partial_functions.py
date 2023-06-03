from typing import Callable, TypeVar


T = TypeVar("T")


identity: Callable[[T], T] = lambda x: x




add: Callable[[int, int], int] = lambda x, y: x + y

add2: Callable[[int], int] = lambda x: add(2, x)



print(add(2, 3))
print(add2(3))

print(identity(42))  # 42


