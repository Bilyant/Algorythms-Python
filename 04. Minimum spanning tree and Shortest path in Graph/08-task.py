"""
input data:
4
5
0 - 1 - 10
0 - 2 - 6
0 - 3 - 5
1 - 3 - 15
2 - 3 - 4
"""

nodes = int(input())
edges = int(input())
graph = []

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(' - ')]
    graph.append((first, second, weight))

parent = [x for x in range(nodes)]
total_cost = 0


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


for first, second, weight in sorted(graph, key=lambda x: x[2]):
    first_node_root = find_root(parent, first)
    second_node_root = find_root(parent, second)

    if first_node_root == second_node_root:
        continue

    parent[first_node_root] = second_node_root
    total_cost += weight

print(f'Total cost: {total_cost}')
