# 'v' == visited
# 'e' == exit
# '*' == invalid cell


def find_path(labyrinth, row_idx, col_idx, direction, path):

    if row_idx < 0 or col_idx < 0 or row_idx >= len(labyrinth) or col_idx >= len(labyrinth[0]):
        return

    if labyrinth[row_idx][col_idx] == '*' or labyrinth[row_idx][col_idx] == 'v':
        return

    path.append(direction)

    if labyrinth[row_idx][col_idx] == 'e':
        print(''.join(path))
    else:
        labyrinth[row_idx][col_idx] = 'v'

        find_path(labyrinth, row_idx - 1, col_idx, 'U', path)
        find_path(labyrinth, row_idx + 1, col_idx, 'D', path)
        find_path(labyrinth, row_idx, col_idx - 1, 'L', path)
        find_path(labyrinth, row_idx, col_idx + 1, 'R', path)
        labyrinth[row_idx][col_idx] = '-'

    path.pop()


rows = int(input())
cols = int(input())
labyrinth = []

for row in range(rows):
    labyrinth.append([ch for ch in input()])

find_path(labyrinth, 0, 0, '', [])
