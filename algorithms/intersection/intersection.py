from typing import List


def intersection(a: list[int], b: list[int])-> list[int]:
    """method to get the intersect of two lists"""
    a, b = sorted(a), sorted(b)
    inter: List[int] = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            inter.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return inter



list1 = [1, 6, 2, 9, 6, 3, 5, 11]
list2 = [7, 7, 9, 8, 2, 3, 12, 4]




if __name__ == '__main__':
    
    print(intersection(list1, list2)) # [2, 3, 9]
 