"""
Finding the shortest path from destination a to destination b in an unweighted graph
"""

from collections import deque


def find_path_by_parent(graph, start_node, destination_node):
    visited = [False] * len(graph)
    parent = [None] * len(graph)

    visited[start_node] = True
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node == destination_node:
            break
        for child in graph[node]:
            if visited[child]:
                continue
            visited[child] = True
            queue.append(child)
            parent[child] = node

    return parent


def reconstruct_path(parent, destination_node):
    path = deque()
    node = destination_node
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    return path


input_data = [
    8,
    10,
    '1 2',
    '1 4',
    '2 3',
    '4 5',
    '5 8',
    '5 6',
    '5 7',
    '5 8',
    '6 7',
    '7 8',
    1,
    7,
]

nodes_count = input_data[0]
edges_count = input_data[1]
start_node = input_data[-2]
destination_node = input_data[-1]
graph = []
[graph.append([]) for _ in range(nodes_count + 1)]

for i in range(2, len(input_data) - 2):
    source, destination = [int(n) for n in input_data[i].split()]
    graph[source].append(destination)

parent = find_path_by_parent(graph, start_node, destination_node)
print(parent)
path = reconstruct_path(parent, destination_node)
print(path)

print(f'Shortest path length is {len(path) - 1}')
print(*path, sep=' ')
