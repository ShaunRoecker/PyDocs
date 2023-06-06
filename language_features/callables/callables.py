from typing import Callable


# Types of Callables:

# 1. built-in functions
# 2. built-in methods
# 3. user-defined functions
# 4. methods
# 5. classes


print(callable(print)) # True

result = print("hello")
print(result) # None

l = [1, 2, 3]
print(callable(l.append)) # True

from decimal import Decimal
print(callable(Decimal)) # True 


class MyClass:
    def __init__(self, x=0):
        print("initializing...")
        self.counter = x

    def __call__(self, x=1):
        print("updating counter...")
        self.counter += x




callable(MyClass) # True

a = MyClass(100)

callable(a) # True
