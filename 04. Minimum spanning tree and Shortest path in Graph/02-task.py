"""
Dijkstra’s algorithm using a priority queue in weighted graph.
"""

from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


input_data = [
    18,
    '0, 6, 10',
    '0, 8, 12',
    '6, 4, 17',
    '6, 5, 6',
    '8, 5, 3',
    '5, 4, 5',
    '5, 11, 33',
    '8, 2, 14',
    '2, 11, 9',
    '2, 7, 15',
    '4, 1, 20',
    '4, 11, 11',
    '11, 1, 6',
    '11, 7, 20',
    '1, 9, 5',
    '1, 7, 26',
    '7, 9, 3',
    '3, 10, 7',
    0,
    9,
]

edges_count = input_data[0]
graph = {}

for i in range(1, edges_count + 1):
    source, destination, weight = [int(n) for n in input_data[i].split(', ')]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(Edge(source, destination, weight))

start_node = input_data[-2]
target = input_data[-1]

max_node = max(graph.keys())

distance = [float('inf')] * (max_node + 1)
parent = [None] * (max_node + 1)

distance[start_node] = 0
priority_queue = PriorityQueue()
priority_queue.put((0, start_node))

while not priority_queue.empty():
    min_distance, node = priority_queue.get()
    if node == target:
        break
    for edge in graph[node]:
        new_distance = min_distance + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = node
            priority_queue.put((new_distance, edge.destination))

if distance[target] == float('inf'):
    print('There is no such path.')
else:
    print(distance[target])

    path = deque()
    node = target
    while node is not None:
        path.append(node)
        node = parent[node]
    print(*path, sep=' ')
