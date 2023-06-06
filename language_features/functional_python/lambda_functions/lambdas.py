

f1 = lambda x: x + 2
print(f1(2)) # 4


f2 = lambda x, *args, y, **kwargs: (x, *args, y, kwargs)
print(f2(1, "a", "b", y=100, a=10, b=20)) # (1, 'a', 'b', 100, {'a': 10, 'b': 20})


def apply_func(x, fn):
    return fn(x)


apply_func(5, lambda x: x**2)  # 25

























