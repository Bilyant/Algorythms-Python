"""

Write an implementation of Bubble Sort. You should read an array of integers and sort them.

Input:
5 4 3 2 1 0

"""


def bubble_sort(collection):
    are_sorted = False
    count = 0

    while not are_sorted:

        are_sorted = True
        for idx in range(1, len(collection) - count):
            firstN = collection[idx - 1]
            nextN = collection[idx]

            if firstN > nextN:
                collection[idx], collection[idx - 1] = collection[idx - 1], collection[idx]
                are_sorted = False
        count += 1


numbers = [int(n) for n in input().split(' ')]
bubble_sort(numbers)
print(*numbers, sep=' ')
