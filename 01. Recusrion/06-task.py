def reverse_my_array(array: [], idx):

    if idx >= int(len(array) / 2):
        return ' '.join([str(n) for n in array])

    array[idx], array[-idx - 1] = array[-idx - 1], array[idx]
    return reverse_my_array(array, idx + 1)


arr = [n for n in range(1, 7)]
print(reverse_my_array(arr, 0))
