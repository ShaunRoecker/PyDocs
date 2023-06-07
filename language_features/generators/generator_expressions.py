

def factorial(n: int)-> int:
    return 1 if n < 2 else n * factorial(n-1)


gen_obj = (factorial(n) for n in range(10))