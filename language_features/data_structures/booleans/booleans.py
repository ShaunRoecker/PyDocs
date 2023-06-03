


True == 1 # True
True is 1 # False

False == 0 # True
False is 0 # False

# bool is a subclass of int
is_sub = issubclass(bool, int)
is_sub

#type(True), id(True, int(True))    # <class 'bool'>  94733159715872  1
#type(False), id(False), int(False) # <class 'bool'>  94733159715840  0

type(3 < 4) # <class 'bool'>

(3 < 4) == True  # True
(3 < 4) is True  # True

None is False # False
None == False # False

bool(0)  # False
bool(1) # True
bool(100) # True
bool(-1) # True

# All objects in Python have an associated 'truth' value

# Every object has a True truth value, except:
# 1. None
# 2. False
# 3. 0 in any numeric type(e.g. 0, 0.0, 0+0j, ...)
# 4. Empty sequences(list, tuple, string, ...)
# 5. Empyy mapping types (dict, set, ...)
# 6. Custom classes that implement a __bool__ 
#       or __len__ method that returns False or 0


# __bool__ implementation in the int class:
def __bool__(self):
    return self != 0


bool([1, 2, 3])  # ==> True
bool([]) # ==> False
bool(None) # ==> False

bool('abc') # ==> True
bool('') 

    
from decimal import Decimal
from fractions import Fraction

bool(Fraction(0, 1))  # False
bool(Fraction(1, 2))  # True

bool(Decimal('0.0'))  # False
bool(Decimal('1.2'))  # True


# Commutative
# A or B == B or A
# A and B == B and A

# Distributive
# A and (B or C) == (A and B) or (A and C)

# Associative
# A or (B or C) == (A or B) or C


# Operator precedence (highest to lowest)
# < > <= >= == != in is  <highest precedence
# not
# and 
# or   <lowest precedence


# True or (True and False)

a = 10
b = 0

# if a/b > 2:
#     print("a is at least twice b")

 
if b and a / b > 2:
    print("a is at least twice b")

import string


a = 'c'
print(a in string.ascii_uppercase)

name = "Bob"
if len(name) and name[0] in string.digits:
    print("Name cannot start with a digit.")


# trick to prevent divide-by-zero error
# if a == 0, then x will be zero
a = 0
total = 10
x = a and total/a

_list = []

avg = len(_list) and sum(_list) / len(_list)

print(avg)

print(not []) # True


# Python returns the objects, not the truthy value 
#  with 'and' and 'or' statements
print(None or [0]) # [0]


s1 = None
s2 = ""
s3 = "abc"

# print(s1[0])  both these throw errors
# print(s2[0])  <--
print(s3[0]) # a

print((s1 and s1[0]) or 'n/a') # n/a
print((s2 and s2[0]) or 'n/a') # n/a
print((s3 and s3[0]) or 'n/a') # a


print('key1' in {'key1': 1}) # True
print(1 in {'key1': 1}) # False



