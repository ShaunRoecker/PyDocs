import decimal
from decimal import Decimal
import sys



a = 3.1415
b = Decimal(str(a))

print(sys.getsizeof(a)) # 24
print(sys.getsizeof(b)) # 104



import time

def run_float(n=1):
    for i in range(n):
        a = 3.1415


def run_decimal(n=1):
    for i in range(n):
        a = Decimal('3.1415')


n = 1000000

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print("float: ", end-start)  # float:  0.5165714019967709

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print("decimal: ", end-start) # decimal:  4.055002256998705





