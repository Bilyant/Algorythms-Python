"""
Depth-First search (DFS)
"""

graph = {
    1: [19, 21, 14],
    19: [7, 12, 31, 21],
    7: [1],
    12: [],
    31: [21],
    21: [14],
    14: [6, 23],
    23: [21],
    6: [],
}

visited_nodes = set()


def dfs_search(node, graph, visited_nodes):
    if node in visited_nodes:
        return

    visited_nodes.add(node)

    for child in graph[node]:
        dfs_search(child, graph, visited_nodes)

    print(node, end=' ')


for node in graph:
    dfs_search(node, graph, visited_nodes)
