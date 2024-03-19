"""
Sort an array of elements using the famous quicksort.

Input:
6 5 4 3 2 1 0
"""


def quick_sort(start, end, collection):
    pivot = start
    left_idx = pivot + 1
    right_idx = end

    if start >= end:
        return

    while left_idx <= right_idx:

        if collection[left_idx] > collection[pivot] > collection[right_idx]:
            collection[left_idx], collection[right_idx] = collection[right_idx], collection[left_idx]
        if collection[left_idx] <= collection[pivot]:
            left_idx += 1
        if collection[right_idx] >= collection[pivot]:
            right_idx -= 1

    collection[pivot], collection[right_idx] = collection[right_idx], collection[pivot]
    quick_sort(start, right_idx - 1, collection)
    quick_sort(right_idx + 1, end, collection)


numbers = [int(n) for n in input().split()]
quick_sort(0, len(numbers) - 1, numbers)
print(*numbers, sep=' ')
