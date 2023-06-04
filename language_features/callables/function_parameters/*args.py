



def func1(a, b, *args):
    print(f"a: {a}, b: {b}, c: {args}")

func1(1, 2, 3, 4, 5, 6, 7)
# a: 1, b: 2, c: (3, 4, 5, 6, 7)



# it's not required to name it *args

def func2(a, b, *c):
    # c_args = ", ".join(c)
    print(f"a: {a}, b: {b}, c: {c}")

func2(1, 2, 3, 4, 5, 6, 7)
# a: 1, b: 2, c: (3, 4, 5, 6, 7)



def avg(*args):
    count = len(args)
    total = sum(args)
    return count and total/count

print(avg(1, 2, 3)) # 2.0
print(avg(0)) # 0.0
print(avg()) # 0

# In case you don't want to return zero, but also don't
# want to throw a zero-division error, the below way will
# force at least one argument, an error if args missing

def avg2(num, *args):
    count = len(args) + 1
    total = sum(args) + num
    return total/count

print(avg2()) # TypeError: avg2() missing 1 required positional argument: 'num'
print(avg2(1, 2, 3)) # 2.0



