from fractions import Fraction
import math



a = Fraction("22/7")

print(float(a))

a = 0.1

print(a) # 0.1
print(format(a, ".15f")) # 0.100000000000000
print(format(a, ".25f")) # 0.1000000000000000055511151

############################################################
############################################################

a = 0.1 + 0.1 + 0.1
b = 0.3

print(a == b) # False
# To fix this... never use == on floats

print(math.isclose(a, b)) # True

#for large numbers, then look at relative tolerances
#for small numbers, then look at absolute tolerances

print(math.isclose(a, b, rel_tol=0.01, abs_tol=0.01))

print(math.isclose(1.19, 1.19000001)) # False

############################################################
############################################################

x = 10000.01
y = 10000.02

print(round(x, 3) == round(y, 3))

print(y / x)

print(format(x, '.25f')) # 0.1000000000000000055511151


# 0.1 and 0.3 do not have finite binary representations,



# Coercing Floats to Integer

# Float --> Integer == Data loss

# 1. Trucation
print("Trucation")
# Truncation simple return the integer part of the number
print(math.trunc(10.4) == 10) # true
print(int(10.4) == 10) # true


# 2. Floor
print("Floor")
# The floor of a number is the largest integer less than 
# or equal to the number
print(math.floor(-10.4))  # -11
print(math.floor(10.4)) # 10

# Floor division
print(10 // 3) # 3


# 3. Ceiling
print("Ceiling")
# The ceiling of a number is the smallest integer greater than 
# (or equal to) the number

print(math.ceil(10.1)) # 11
print(math.ceil(-10.1)) # -10


#Rounding

n = round(10.2, 0)
print(n) # 10.0

print(round(1.25, 1)) # 1.2


# Banker's Rounding (least biases)
print(round(15, -1))
print(round(25, -1))

# another implementation of bankers rounding (only for ints and not for negatives)
bankers = lambda x: int(x + 0.5)

print(bankers(10.3))
print(bankers(10.9))



print(round(1.8888, 3), round(1.8888, 2), round(1.8888, 1), round(1.8888, 0))


def _round(x):
    from math import copysign
    return int(x + 0.5 * copysign(1, x))  # math.copysign(x, y) returns x with the sign (-/+) of y


print(round(1.5), _round(1.5)) # 2  2
print(round(2.5), _round(2.5)) # 2  3



