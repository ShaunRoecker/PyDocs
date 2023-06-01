import sys
import time
import math


print(type(100))
# <class 'int'>


print(sys.getsizeof(0))
# 24

print(sys.getsizeof(1))
# 28

print(sys.getsizeof(2**1000))
# 160


def calc(a: int)-> None:
    for i in range(10000000):
        a * 2


def time_calc(n: int)-> None:
    start = time.perf_counter()
    calc(n)
    end = time.perf_counter()
    print(end - start) 



# time_calc(10)       # 0.3657017179994
# time_calc(2**100)   # 0.6512562779998916
# time_calc(2**10000) # 4.181725463000475



#  155 / 4 = 38 with remainder 3

#  155 = 4 * 38 + 3

#              floor       modulo (mod)
#  155 = 4 * (155 // 4) + (155 % 4)

print(math.floor(3.14)) # 3
print(math.floor(1.9999)) # 1
print(math.floor(2)) # 2
print(math.floor(-3.1)) # -4



(135 / 4) == 4 * (135 // 4) + (135 % 4)


# a = b * (a // b) + a % b


print(10/5) # 2.0

print(10//5) # 2

int_base10_123 = int("123")

# The base defaults to 10

int_base2_1010 = int("1010", base=2)

print(int_base10_123, int_base2_1010) # (123, 10)


print(int("A12F", base=16)) # 41263

print(bin(100)) # 0b1100100

print(oct(100)) # 0o144

print(hex(100)) # 0x64


a = 0b1100100
b = 0o144
c = 0x64

print(a, b, c) # 100 100 100


# represent 232 in a different representation

n = 232 # 232 is what in base 5
b = 5

# a = b * (a // b) + (a % b)









