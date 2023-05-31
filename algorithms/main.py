from time import time


import intersection.intersection as inter
from sorting.merge_sort import merge_sort



list1 = [2, 6, 8, 4, 3, 5, 7, 9, 5, 3, 2, 5, 8]



def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

