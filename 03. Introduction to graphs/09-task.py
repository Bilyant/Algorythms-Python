def calc_salary(graph, node, salaries):
    if salaries[node] is not None:
        return salaries[node]
    if len(graph[node]) == 0:
        salaries[node] = 1
        return 1

    salary = 0
    for employee in graph[node]:
        salary += calc_salary(graph, employee, salaries)

    salaries[node] = salary
    return salary


input_data = [
    6,
    'NNNNNN',
    'YNYNNY',
    'YNNNNY',
    'NNNNNN',
    'YNYNNN',
    'YNNYNN',
]
number = input_data[0]
matrix = []
graph = []
salaries = [None] * number
total = 0

for i in range(1, number + 1):
    matrix.append(list(input_data[i]))

for row in range(number):
    node = []
    for col in range(number):
        if matrix[row][col] == 'Y':
            node.append(col)
    graph.append(node)

print(graph)

for node in range(len(graph)):
    salary = calc_salary(graph, node, salaries)
    total += salary

print(total)
