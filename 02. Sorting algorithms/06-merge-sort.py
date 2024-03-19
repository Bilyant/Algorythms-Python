"""
Sort an array of elements using the famous merge sort.

Input:
10 9 8 7 6 5 4 3 2 1
"""


def merge_arrays(left_side, right_side):
    result = [None] * (len(left_side) + len(right_side))
    left_idx = 0
    right_idx = 0
    result_idx = 0

    while left_idx < len(left_side) and right_idx < len(right_side):
        if left_side[left_idx] < right_side[right_idx]:
            result[result_idx] = left_side[left_idx]
            left_idx += 1
        else:
            result[result_idx] = right_side[right_idx]
            right_idx += 1
        result_idx += 1

    while left_idx < len(left_side):
        result[result_idx] = left_side[left_idx]
        left_idx += 1
        result_idx += 1

    while right_idx < len(right_side):
        result[result_idx] = right_side[right_idx]
        right_idx += 1
        result_idx += 1

    return result


def merge_sort(collection):

    if len(collection) == 1:
        return collection

    middle = len(collection) // 2
    left_side = collection[:middle]
    right_side = collection[middle:]

    return merge_arrays(merge_sort(left_side), merge_sort(right_side))


numbers = [int(n) for n in input().split()]
print(merge_sort(numbers))
