from collections import defaultdict


def dfs(graph, start):
    stack = list(start)
    visited = set()

    while stack:
        current_node = stack.pop()
        print(current_node)
        for node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)


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

dfs(graph, "1")
