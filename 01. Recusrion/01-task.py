def find_sum(numbers, idx):

    if idx == len(numbers) - 1:
        return numbers[idx]
    return numbers[idx] + find_sum(numbers, idx + 1)


numbers = [n for n in range(1, 5)]
print(find_sum(numbers, 0))
