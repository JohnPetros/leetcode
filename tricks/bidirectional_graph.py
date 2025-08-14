from collections import defaultdict

edges = [
    [1, 6],
    [1, 5],
    [2, 5],
    [3, 4],
]

graph = defaultdict(list)

for first_node, second_node in edges:
    graph[first_node].append(second_node)
    graph[second_node].append(first_node)
