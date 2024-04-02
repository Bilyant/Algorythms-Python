"""
Bellman-Ford algorithm - it is used to find the shortest path in a graph when edges have negative values.
"""

from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


input_data = [
    6,
    8,
    '1 2 8',
    '1 3 10',
    '2 4 1',
    '3 6 2',
    '4 3 -4',
    '4 6 -1',
    '6 5 -2',
    '5 3 1',
    1,
    6,
]

nodes_count = input_data[0]
edges_count = input_data[1]
graph = []

for i in range(2, edges_count + 2):
    source, destination, weight = [int(n) for n in input_data[i].split()]
    graph.append(Edge(source, destination, weight))

start_node = input_data[-2]
target = input_data[-1]

distance = [float('inf')] * (nodes_count + 1)
distance[start_node] = 0
parent = [None] * (nodes_count + 1)

for _ in range(nodes_count - 1):
    updated = False
    for edge in graph:
        if distance[edge.source] == float('inf'):
            continue
        new_distance = distance[edge.source] + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = edge.source
            updated = True
    if not updated:
        break

for edge in graph:
    new_distance = distance[edge.source] + edge.weight
    if new_distance < distance[edge.destination]:
        print('Negative Cycle Detected')
        break
else:
    path = deque()
    node = target

    while node is not None:
        path.appendleft(node)
        node = parent[node]

    print(*path, sep=' ')
    print(distance[target])
