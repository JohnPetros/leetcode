from collections import defaultdict

edges = [
    [1, 6],
    [1, 5],
    [2, 5],
    [2, 7],
    [3, 6],
    [3, 8],
    [3, 4],
]

graph = defaultdict(list)

for first_node, second_node in edges:
    graph[first_node].append(second_node)
