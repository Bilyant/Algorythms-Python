def dfs(node, destination, graph, visited):
    if node in visited:
        return
    visited.add(node)
    if node == destination:
        return
    for child in graph[node]:
        dfs(child, destination, graph, visited)


def path_exists(source, destination, graph):
    visited = set()
    dfs(source, destination, graph, visited)
    return destination in visited


input_data = [
    8,
    '1 -> 2 5 4',
    '2 -> 1 3',
    '3 -> 2 5',
    '4 -> 1',
    '5 -> 1 3',
    '6 -> 7 8',
    '7 -> 6 8',
    '8 -> 6 7',
]

nodes = input_data[0]
graph = {}
edges = []

for i in range(1, nodes + 1):
    data = input_data[i].split(' -> ')
    parent = int(data[0])
    children = [int(n) for n in data[1] if n != ' ']
    graph[parent] = children
    for child in children:
        edges.append((parent, child))

for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if destination not in graph[source] or source not in graph[destination]:
        continue
    graph[source].remove(destination)
    graph[destination].remove(source)

    if path_exists(source, destination, graph):
        print(source, destination)
    else:
        graph[source].append(destination)
        graph[destination].append(source)
