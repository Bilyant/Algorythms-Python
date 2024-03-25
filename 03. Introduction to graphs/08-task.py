"""
input example 1:
A-F
F-D
D-A
End

input example 2:
E-Q
Q-P
P-B
End
"""


def find_cycles(graph, node, visited, path):
    if node in path:
        raise Exception
    if node in visited:
        return

    visited.add(node)
    path.add(node)

    for child in graph[node]:
        find_cycles(graph, child, visited, path)

    path.remove(node)


line = input()
graph = {}

while line != 'End':
    parent, child = line.split('-')
    if parent not in graph:
        graph[parent] = []
    if child not in graph:
        graph[child] = []
    graph[parent].append(child)
    line = input()

visited = set()
print(graph)

try:
    for node in graph:
        path = set()
        find_cycles(graph, node, visited, path)
    print('Acyclic: Yes')
except Exception:
    print('Acyclic: No')
