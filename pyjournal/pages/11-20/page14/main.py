import ctypes
import gc
from collections import namedtuple

# Circular references

def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
    return "Not found"


class A:
    def __init__(self):
        self.b = B(self)
        print(f"A: self: {hex(id(self))}, b: {hex(id(self.b))}")


class B:
    def __init__(self, a):
        self.a = a
        print(f"B: self: {hex(id(self))}, b: {hex(id(self.a))}")



gc.disable()


my_var = A()

# B: self: 0x7f7f3ff73910, b: 0x7f7f3ff73f40
# A: self: 0x7f7f3ff73f40, b: 0x7f7f3ff73910


print(hex(id(my_var)))  # 0x7f7f3ff73f40


print(hex(id(my_var.b)))  # 0x7f7f3ff73f40
print(hex(id(my_var.b.a)))  # 0x7f7f3ff73f40


a_id = id(my_var)
b_id = id(my_var.b)


print(ref_count(a_id)) # 2
print(ref_count(b_id)) # 1



my_list = [1, 2, 3]
print(type(my_list))




# identity operator

var_1 = 43

var_2 = 45

var3 = var_2

print(var_1 is var_2) # False

print(var_2 == var3) # True


