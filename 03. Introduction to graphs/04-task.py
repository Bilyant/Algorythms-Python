"""
Traverse a graph and find its connected components (nodes connected either directly,
or through other nodes)

example input:

9
3 6
3 4 5 6
8
0 1 5
1 6
1 3
0 1 4

2

"""


def find_connections(graph, node_idx, visited, component: []):

    if visited[node_idx]:
        return

    visited[node_idx] = True

    for child in graph[node_idx]:
        find_connections(graph, child, visited, component,)

    component.append(node_idx)


graph = []
connections = []
nodes_count = int(input())

for _ in range(nodes_count):
    line = input()
    nodes = [int(n) for n in line.split(' ')] if line else []
    graph.append(nodes)

visited = [False] * len(graph)

for idx in range(len(graph)):
    print(f'Idx: {idx}, nodes: {", ".join([str(n) for n in graph[idx]])}')


for node_idx in range(len(graph)):
    component = []
    find_connections(graph, node_idx, visited, component)
    if component:
        print(f'Connected component: {" ".join([str(n) for n in component])}')

