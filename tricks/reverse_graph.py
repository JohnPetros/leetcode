from collections import defaultdict

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B"],
}

reverse_grafo = defaultdict(list)

for first_node, neighbors in graph.items():
    for second_node in neighbors:
        reverse_grafo[second_node].append(first_node)

print(reverse_grafo)


graph = {
    "A": {"B": 1, "C": 4},
    "B": {"C": 2, "D": 5},
    "C": {"D": 1},
    "D": {},
}

reverse_grafo = defaultdict(dict)

for first_node, neighbors in graph.items():
    for second_node, weight in neighbors.items():
        reverse_grafo[second_node][first_node] = weight

print(reverse_grafo)
