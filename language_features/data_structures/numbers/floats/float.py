from fractions import Fraction



a = Fraction("22/7")

print(float(a))

a = 0.1

print(a) # 0.1
print(format(a, ".15f")) # 0.100000000000000
print(format(a, ".25f")) # 0.1000000000000000055511151

a = 0.1 + 0.1 + 0.1
b = 0.3

print(a == b) # False

