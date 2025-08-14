from collections import defaultdict

edges = [
    [0, 1, 2],  # (first_node, second_node, weight)
    [1, 2, 3],
    [1, 3, 1],
    [1, 4, 3],
    [2, 4, 2],
    [7, 9, 7],
    [9, 8, 5],
]

graph = defaultdict(dict)

for first_node, second_node, weight in edges:
    graph[first_node][second_node] = weight

print(graph)
