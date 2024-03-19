"""

Write an implementation of Selection Sort. You should read an array of integers and sort them.

Input:
5 4 3 2 1

"""


def selection_sort(numbers):
    for idx in range(len(numbers)):
        current_number = numbers[idx]
        smallest_num_idx = None

        for next_idx in range(idx, len(numbers)):
            if numbers[next_idx] < current_number:
                smallest_num_idx = next_idx

        if smallest_num_idx:
            numbers[idx], numbers[smallest_num_idx] = numbers[smallest_num_idx], numbers[idx]
        idx += 1


collection = [int(n) for n in input().split(' ')]
selection_sort(collection)

print(*collection, sep=' ')
