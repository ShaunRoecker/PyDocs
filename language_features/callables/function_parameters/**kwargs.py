


# We can make keyword arguments mandatory

def func(a, b, *args, d):
    print(f"a: {a}, b: {b}, args: {args}, d: {d}")


# func(1, 2, 3, 4, 5, 6)
# TypeError: func() missing 1 required keyword-only argument: 'd'


def func2(a, b=1, *args, d, e=True):
    print(f"a: {a}, b: {b}, args: {args}, d: {d}, e: {e}")

# d is a mandatory keyword argument
func2(1, 2, 3, 4, d=5)
# a: 1, b: 2, args: (3, 4), d: 5, e: True

#func2(1, 2, 3, 4, d=5, False)
# SyntaxError: positional argument follows keyword argument

func2(1, 2, 3, 4, d=5, e=False)
# a: 1, b: 2, args: (3, 4), d: 5, e: False



### **kwargs ##############################

def func_with_kwargs(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs, sep="\n")


func_with_kwargs(1, 2, 3, 4, 5, 6)
# 1 2 (3, 4, 5, 6) {}

func_with_kwargs(1, 2, 3, 4, 5, kwarg1=6, kwarg2="arg", kwarg3=10)
# 1 2 (3, 4, 5) {'kwarg1': 6, 'kwarg2': 'arg', 'kwarg3': 10}


def func_with_kwargs2(a, b=2, *args, **kwargs):
    print(a, b, args, [*kwargs])

func_with_kwargs2(1, 2, 3, 4, 5, kwarg1=6, kwarg2="arg", kwarg3=10)
# 1 2 (3, 4, 5) ['kwarg1', 'kwarg2', 'kwarg3']


def func3(**others):
    print(others)

func3(a=1, b=2, c=3)
# {'a': 1, 'b': 2, 'c': 3}


def calc_hi_low_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args)
    lo = min(args) if len(args) > 0 else 0
    avg = (hi + lo) / 2
    if log_to_console:
        print(f"Hi: {hi}, Lo: {lo}, AVG: {avg}")
    return avg



def time_it(fn, *args, rep=1, **kwargs):
    import time
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return rep and (end - start) / rep


from datetime import datetime

def log(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    print(f"{dt}: {msg}")

#  Be very careful setting default parameters to mutable
#  collections, as the are created when the function is
# created, and they will always refer to the same collection
#  (that can be changed), this can cause problems.
#  Its often better to set it to  None, so it will create 
#  the collection each time it is called.

def add_item(name, quantity, unit=1, grocery_list=None):
    """
    method to add an item to a provided list. If no list provided,
    a list is created.
    """
    if not grocery_list:
        grocery_list = []
    grocery_list.append(f"{name} ({quantity} {unit})")
    return grocery_list


print(add_item.__doc__)


