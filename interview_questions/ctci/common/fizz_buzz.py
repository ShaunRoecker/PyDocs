


def fizzbuzz(n: int, printer: bool = False)-> list[str]:
    def map_fizz(n: int)-> str:
        if n % 3 == 0 and n % 5 == 0:
            return "fizzbuzz"
        elif n % 3 == 0:
            return "fizz"
        elif n % 5 == 0:
            return "buzz"
        else:
            return str(n)
    list_fb = list(map(lambda x: map_fizz(x), range(1, n)))
    # or --> list_fb = [map_fizz(x) for x in range(1, n)]
    if printer:
        for i in list_fb:
            print(i)
        return list_fb
    else:
        return list_fb



fizzbuzz(16, True)
print(fizzbuzz(16))

