"""

Write an implementation of Insertion Sort. You should read an array of integers and sort them.

Input:
5 4 3 2 1 0

"""


def insertion_sort(collection):
    for i in range(1, len(collection)):
        for j in range(i, 0, -1):

            if collection[j] < collection[j - 1]:
                collection[j], collection[j - 1] = collection[j - 1], collection[j]
            else:
                break


numbers = [int(n) for n in input().split(' ')]
insertion_sort(numbers)
print(*numbers, sep=' ')
