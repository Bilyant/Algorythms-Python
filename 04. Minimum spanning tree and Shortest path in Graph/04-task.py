"""
Kruskal's algorithm for finding a minimum spanning tree in a forest

input data:
11
0, 3, 9
0, 5, 4
0, 8, 5
1, 4, 8
1, 7, 7
2, 6, 12
3, 5, 2
3, 6, 8
3, 8, 20
4, 7, 10
6, 8, 7
"""


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


edges = int(input())
graph = []
max_node = float('-inf')

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(', ')]
    graph.append(Edge(first, second, weight))
    max_node = max(first, second, max_node)

parent = [x for x in range(max_node + 1)]
forest = []

for edge in sorted(graph, key=lambda e: e.weight):
    first_node_root = find_root(parent, edge.first)
    second_node_root = find_root(parent, edge.second)
    if first_node_root != second_node_root:
        parent[first_node_root] = second_node_root
        forest.append(edge)

print(parent)
for edge in forest:
    print(f'{edge.first} - {edge.second}')
