def find_dependencies(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0
        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1
    return result


def find_node_without_dependecies(dependencies):
    for node, node_dependencies in dependencies.items():
        if node_dependencies == 0:
            return node
    return None


nodes_count = int(input())
graph = {}

for _ in range(nodes_count):
    line = input().split(' ->')
    children = line[1].strip().split(', ') if line[1] else []
    graph[line[0]] = children

dependencies = find_dependencies(graph)
is_valid = True
sorted_nodes = []

while dependencies:
    node_to_remove = find_node_without_dependecies(dependencies)
    if not node_to_remove:
        is_valid = False
        break
    dependencies.pop(node_to_remove)
    sorted_nodes.append(node_to_remove)
    for child in graph[node_to_remove]:
        dependencies[child] -= 1

if is_valid:
    print(f'Topological sorting: {", ".join(sorted_nodes)}')
else:
    print('Invalid topological sorting')
