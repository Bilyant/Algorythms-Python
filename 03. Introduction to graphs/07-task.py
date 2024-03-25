"""
input:
6
8
aacccaac
baaaaccc
baabaccc
bbdaaccc
ccdccccc
ccdccccc

"""


def find_cycles(graph, node, visited, connected_nodes):
    connected_nodes.append(node)
    if node in visited:
        return
    if node not in graph:
        return

    visited.add(node)
    for child in graph[node]:
        find_cycles(graph, child, visited, connected_nodes)

    return connected_nodes[0] == connected_nodes[-1]


line = input()
graph = {}
visited = set()
is_acyclic = False

while line != 'End':
    parent, child = line.split('-')
    if parent not in graph:
        graph[parent] = []
    graph[parent].append(child)
    line = input()

for node in graph:
    visited = set()
    is_acyclic = find_cycles(graph, node, visited, [])
    if is_acyclic:
        break

if is_acyclic:
    print('Acyclic: No')
else:
    print('Acyclic: Yes')
