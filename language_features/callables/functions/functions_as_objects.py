# Function Introspection


# Functions are first-class objects

def my_func(a, b):
    return a + b

# def func(
#         a: "mandatory positional", 
#         b: "mandatory positional" =1, 
#         c=2, 
#         *args: "add extra positional here", 
#         kw1, 
#         kw2=100, 
#         kw3=200, 
#         **kwargs: "provide extra kw-only here"
#     )-> "does nothing":
#     """This function does nothing but does have various parameters
#     and annotations
#     """
#     i = 10
#     j = 20




# function have attributes...
# __doc__
# __annotations__

# We can attach our own attributes as well

my_func.category = "math"
my_func.sub_category = "arithmetic"


print(my_func.category) # math
print(my_func.sub_category) # arithmetic

# The dir function

# dir() is a built-in function  that, given an object as an argument, 
# will return a list of valid attributes for that object

print(dir(my_func))

# [
# '__annotations__', 
# '__builtins__', 
# '__call__', 
# '__class__', 
# '__closure__', 
# '__code__',       <-- This __code__ object has various props, which include 
                            # "co_varnames"


# '__defaults__',   <-- tuple containing positional parameter defaults
# '__delattr__',    
# '__dict__', 
# '__dir__', 
# '__doc__', 
# '__eq__', 
# '__format__', 
# '__ge__',
#  '__get__',
#  '__getattribute__',
#  '__globals__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__kwdefaults__',    <-- dictionary containing positional parameter defaults
#  '__le__',
#  '__lt__', 
# '__module__', 
# '__name__',    <-- name of the function
#  '__ne__', 
# '__new__', 
# '__qualname__', 
# '__reduce__',
#  '__reduce_ex__', 
# '__repr__',
#  '__setattr__',
#  '__sizeof__', 
# '__str__',
#  '__subclasshook__',
#  'category', 
# 'sub_category'
# ]


# The inspect module

from inspect import *

print(ismethod(my_func)) # False
print(isfunction(my_func)) # True
print(isroutine(my_func)) # True


print(getsource(my_func)) # a string containing our entire def statement, including annotations, docstrings, etc.
# def my_func(a, b):
#     return a + b

print(getmodule(my_func)) 
# <module '__main__' from '/home/shaun/dev/python/pydocs/language_features/callables/functions/functions_as_objects.py'>


print(getcomments(my_func)) # None

# Callable Signature

sig = signature(my_func) # (a, b)
# Creates a signature instance

print(sig.parameters) # OrderedDict([('a', <Parameter "a">), ('b', <Parameter "b">)])


# func inspection

print(func.__annotations__)
#{'a': 'mandatory positional', 
# 'b': 'mandatory positional', 
# 'args': 'add extra positional here', 
# 'kwargs': 'provide extra kw-only here', 
# 'return': 'does nothing'}

print(func.__doc__)
# This function does nothing but does have various parameters
    # and annotations

print(func.__name__) # func

print(func.__defaults__) # (1, 2)

func_code = func.__code__
print(func_code.co_argcount) # 3
print(func_code.co_consts)
 # ('This function does nothing but does have various parameters\n    and annotations\n    ', 10, 20, None)

print(func_code.co_name) # func
print(func_code.co_varnames) # ('a', 'b', 'c', 'kw1', 'kw2', 'kw3', 'args', 'kwargs', 'i', 'j')


class MyClass:
    def f(self):
        pass


print(isfunction(MyClass.f)) # True
myclass = MyClass()
print(isfunction(myclass))


print(getsource(getsourcelines))

sig = signature(func)

print(sig.parameters)
print("\n\n")

for k, param in sig.parameters.items():
    print("Name: ", param.name)
    print("Default: ", param.default)
    print("Annotation: ", param.annotation)
    print("Kind: ", param.kind)
    print("******************************")
    

