



def bubble_sort(xs: list[int])-> list[int]:
    """bubble sort algorithm to sort a list.
    this algorithm is simple but not very performant"""
    n = len(xs)
    for k in range(1, n - 1):
        for j in range(0, n - k):
            if xs[j] > xs[j + 1]:
                temp = xs[j]      # <-- swapping xs[j] & xs[j + 1]
                xs[j] = xs[j + 1]  # <-
                xs[j + 1] = temp    # <- 
    return xs



list1 = [2, 7, 3, 8, 4, 2, 11, 9, 10, 5]

print(bubble_sort(list1)) # [2, 2, 3, 4, 5, 7, 8, 9, 10, 11]
