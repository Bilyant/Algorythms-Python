"""
input example 1:
8
4
1:4
2:4
3:4 5
4:6
5:3 7 8
6:
7:8
8:
1-6
1-5
5-6
5-8


input example 2:
9
8
11:4
4:12 1
1:12 21 7
7:21
12:4 19
19:1 21
21:14 31
14:14
31:
11-7
11-21
21-4
19-14
1-4
1-11
31-21
11-14
"""

from collections import deque


def bfs(node, target, graph, max_node):
    parent = [None] * (max_node + 1)
    visited = [False] * (max_node + 1)
    queue = deque([node])

    while queue:
        node = queue.popleft()
        if node == target:
            break
        for child in graph[node]:
            if visited[child]:
                continue
            visited[child] = True
            parent[child] = node
            queue.append(child)

    if parent[target]:
        return parent
    return None


def create_path(target, start_node, parent):
    path = deque()
    while target != start_node:
        path.appendleft(target)
        target = parent[target]
    return len(path)


vertices_count = int(input())
pairs_count = int(input())
pairs = []
graph = {}
max_node = float('-inf')

for _ in range(vertices_count):
    line = [n for n in input().split(':')]
    parent = int(line[0])
    if parent not in graph:
        graph[parent] = []
    children = [int(n) for n in line[1].split()] if line[1] else []
    max_node = max(parent, max_node)
    graph[parent].extend(children)

for _ in range(pairs_count):
    pairs.append([int(x) for x in input().split('-')])

for start_node, target in pairs:
    parent = bfs(start_node, target, graph, max_node)
    if parent:
        weight = create_path(target, start_node, parent)
        print(f"{{{start_node}, {target}}} -> {weight}")
    else:
        print(f"{{{start_node}, {target}}} -> -1")
