from fractions import Fraction
import math


x = Fraction(3, 4)
y = Fraction(22, 7)
z = Fraction(6, 10)

print(x + y + z) # 629/140

# options:
Fraction(numerator=0, denominator=1)
Fraction(12.5)
Fraction("10.5")
Fraction(10)

print(x + y / z * x - y) # 43/28

print(x.numerator, x.denominator) # 3 4

x = Fraction(math.pi)

print(x) # 884279719003555/281474976710656

y = Fraction(math.sqrt(2))

print(y) # 6369051672525773/4503599627370496


# ******Warning*****

# 1/ 8 has an exact representation

print(Fraction(0.125) == Fraction(1, 8)) # True

# 3 / 10 does not have an exact float representation

print(Fraction(0.3) == Fraction(3, 10)) # False




# Contraining the demoninator
print(math.pi) # 3.141592653589793

x = Fraction(math.pi) # 884279719003555/281474976710656
x1 = x.limit_denominator(10) # Fraction(22, 7)
print(x1) # 3.142857142857143


x2 = x.limit_denominator(100)  # Fraction(311/99)
print(x2) # 3.1414141414141414


x3 = x.limit_denominator(500)  # Fraction(355/113)
print(x3) # 3.1415929203539825


a = 0.125
print(a)

b = 0.3
print(b)

print(Fraction(b)) # 5404319552844595/18014398509481984

print(format(b, '0.5f')) # 0.30000
print(format(b, '0.15f')) # 0.300000000000000
print(format(b, '0.25f')) # 0.2999999999999999888977698


print(float(x)) # 3.141592653589793
