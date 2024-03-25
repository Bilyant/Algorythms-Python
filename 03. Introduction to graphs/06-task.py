def dfs(matrix, row, col, area_letter):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[1]):
        return False
    if visited[row][col] is True:
        return
    if matrix[row][col] != area_letter:
        return

    visited[row][col] = True
    dfs(matrix, row + 1, col, area_letter)  # down
    dfs(matrix, row - 1, col, area_letter)  # up
    dfs(matrix, row, col + 1, area_letter)  # right
    dfs(matrix, row + 1, col - 1, area_letter)  # left


data_input = [
    6,
    8,
    'aacccaac',
    'baaaaccc',
    'baabaccc',
    'bbdaaccc',
    'ccdccccc',
    'ccdccccc',
]
rows = data_input[0]
cols = data_input[1]
matrix = []
areas = {}
visited = []
total_areas = 0

for i in range(2, rows + 2):
    line = list(data_input[i])
    matrix.append(line)
    visited.append([False] * len(line))

print(*matrix, sep='\n')
print()

for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue
        letter = matrix[row][col]
        dfs(matrix, row, col, letter)
        if letter not in areas:
            areas[letter] = 1
        else:
            areas[letter] += 1
        total_areas += 1

print(f'Areas: {total_areas}')
for key, areas in sorted(areas.items(), key=lambda x: x[0]):
    print(f"Letter '{key}' -> {areas}")
