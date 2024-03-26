def dfs(node, graph, visited):
    if visited[node]:
        return
    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)


input_data = [
    5,
    5,
    '1 - 0',
    '0 - 2',
    '2 - 1',
    '0 - 3',
    '3 - 4',
]

# input_data = [
#     7,
#     8,
#     '0 - 1',
#     '1 - 2',
#     '2 - 0',
#     '1 - 3',
#     '1 - 4',
#     '1 - 6',
#     '3 - 5',
#     '4 - 5',
# ]

buildings_count = input_data[0]
streets_count = input_data[1]
graph = []
[graph.append([]) for _ in range(buildings_count)]
edges = set()
important_streets = []

for i in range(2, len(input_data)):
    first, second = [int(n) for n in input_data[i].split(' - ')]
    graph[first].append(second)
    graph[second].append(first)
    edges.add((min(first, second), max(first, second)))

# print(graph)

print('Important streets: ')

for first, second in edges:
    graph[first].remove(second)
    graph[second].remove(first)

    visited = [False] * buildings_count
    dfs(0, graph, visited)

    if not all(visited):
        print(first, second)

    graph[first].append(second)
    graph[second].append(first)
