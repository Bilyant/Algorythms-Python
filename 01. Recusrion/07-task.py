def nest_loop(num, idx, row: []):

    if idx == num:
        print(*row, sep=' ')
        return

    for n in range(1, num + 1):
        row[idx] = n
        nest_loop(num, idx + 1, row)


num = int(input())
row = [None] * num
nest_loop(num, 0, row)

