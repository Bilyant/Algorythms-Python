def find_path(c_row, c_col, t_row, t_col):

    if c_row >= t_row or c_col >= t_col:
        return 0

    if c_row == t_row - 1 and c_col == t_col - 1:
        return 1

    result = 0
    result += find_path(c_row, c_col + 1, t_row, t_col)  # Right
    result += find_path(c_row + 1, c_col, t_row, t_col)  # Left

    return result


rows = int(input())
cols = int(input())
combinations_count = []

print(find_path(c_row=0, c_col=0, t_row=rows, t_col=cols))
# print(len(combinations_count))
