"""
Example input 1:
5
10
*--*---*--
*--*---*--
*--*****--
*--*---*--
*--*---*--

Example input 2:

4
9
---*---*-
---*---*-
---*---*-
----*-*--

Connected Areas in a Matrix:

Let’s define a connected area in a matrix as an area of cells in
which there is a path between every two cells.
Write a program to find all connected areas in a matrix.

"""


class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


def find_area(figure, row, col):
    if row < 0 or col < 0 or row >= len(figure) or col >= len(figure[0]):
        return 0

    if figure[row][col] != '-':
        return 0

    figure[row][col] = 'v'
    result = 1
    result += find_area(figure, row - 1, col)  # up
    result += find_area(figure, row + 1, col)  # down
    result += find_area(figure, row, col - 1)  # left
    result += find_area(figure, row, col + 1)  # right

    return result


rows = int(input())
cols = int(input())
figure = []
areas = []

for _ in range(rows):
    figure.append([ch for ch in input()])

for row in range(rows):
    for col in range(cols):
        size = find_area(figure, row, col)
        if size:
            areas.append(Area(row, col, size))

areas = sorted(areas, key=lambda area: (-area.size, area.col, area.row))

print(f'Total areas found: {len(areas)}')
for idx, area in enumerate(areas):
    print(f'Area #{idx + 1} at ({area.row}, {area.col}), size: {area.size}')
