import time
import sys



def compare_using_equals(n):
    a = "a long string that is not interned" * 200
    b = "a long string that is not interned" * 200
    for i in range(n):
        if a == b:
            pass


start = time.perf_counter()
compare_using_equals(10000000)
end = time.perf_counter()
print("equality", end - start)

# equality 1.623221672999989


def compare_using_interning(n):
    a = sys.intern("a long string that is interned" * 200)
    b = sys.intern("a long string that is interned" * 200)
    for i in range(n):
        if a is b:
            pass



start = time.perf_counter()
compare_using_interning(10000000)
end = time.perf_counter()
print("interning", end - start)

# interning 0.4476997729998402












