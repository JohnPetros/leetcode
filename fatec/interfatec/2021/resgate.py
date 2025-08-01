from collections import defaultdict

from collections import deque


def bfs_shortest_path_adjacency_graph(graph, start_node, end_node, terrorists):
    queue = deque([(start_node, [start_node])])

    visited = set([start_node])

    while queue:
        current_node, path = queue.popleft()

        if current_node == end_node:
            return path

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                if neighbor not in terrorists:
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))

    return None


start_node = 1
end_node = 6
terrorists = [2, 3]

edges = [
    (1, 2),
    (1, 4),
    (2, 3),
    (2, 5),
    (3, 6),
    (4, 5),
    (5, 6),
]


graph = defaultdict(list)

for first_node, second_node in edges:
    graph[first_node].append(second_node)
    graph[second_node].append(first_node)


path = bfs_shortest_path_adjacency_graph(graph, start_node, end_node, terrorists)
if path is None:
    print("ABORTAR")
else:
    print("PROSSEGUIR")
