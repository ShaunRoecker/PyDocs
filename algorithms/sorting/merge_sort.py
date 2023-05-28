from typing import List, Tuple



def merge_sort(xs: List[int])-> List[int]:
    list_length = len(xs)
    def merge(left: List[int], right: List[int])-> List[int]:
        output = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                output.append(left[i])
                i += 1
            else:
                output.append(right[j])
                j += 1
        output.extend(left[i:])
        output.extend(right[j:])
        return output

    if not xs:
        return []
    elif list_length == 1:
        return xs
    mid = list_length // 2
    left = merge_sort(xs[:mid])
    right = merge_sort(xs[mid:])

    return merge(left, right)





def run_merge_sort():
    unsorted_list = [4, 1, 5, 7, 2, 6, 1, 1, 6, 4, 10, 33, 5, 7, 23]
    print(unsorted_list)
    sorted_list = merge_sort(unsorted_list)
    print(sorted_list)


run_merge_sort()
# [4, 1, 5, 7, 2, 6, 1, 1, 6, 4, 10, 33, 5, 7, 23]
# [1, 1, 1, 2, 4, 4, 5, 5, 6, 6, 7, 7, 10, 23, 33]