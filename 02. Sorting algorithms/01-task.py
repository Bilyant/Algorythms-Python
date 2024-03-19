"""

Implement an algorithm that finds the index of an element in
a sorted array of integers in logarithmic time.

Input:
1 2 3 4 5
1

-1 0 1 2 4
1

"""


def binary_search(target, collection, left_idx, right_idx):
    middle_idx = (left_idx + right_idx) // 2
    middle_el = collection[middle_idx]

    if left_idx > right_idx:
        return -1

    if target == middle_el:
        return

    if target > middle_el:
        left_idx = middle_idx + 1
    else:
        right_idx = middle_idx - 1

    binary_search(target, collection, left_idx, right_idx)
    return middle_idx


numbers = [int(n) for n in input().split(' ')]
target = int(input())
left_idx = 0
right_idx = len(numbers) - 1

found = binary_search(target, numbers, left_idx, right_idx)
if found >= 0:
    print(f'Index of {target} is {found}')
else:
    print('Target is not in the collection')
