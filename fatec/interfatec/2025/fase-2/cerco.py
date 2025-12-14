from collections import defaultdict
from heapq import heappush, heappop


def dijkstra(graph, start_node, end_node):
    # Passo 1: Inicializa as distâncias e predecessores para todos os nós
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        all_nodes.update(neighbors.keys())

    predecessors = {node: None for node in all_nodes}
    distances = {node: float("infinity") for node in all_nodes}
    distances[start_node] = 0
    min_heap = [(0, start_node)]

    while min_heap:
        current_distance, current_node = heappop(min_heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.get(current_node, {}).items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heappush(min_heap, (distance, neighbor))

    # Passo 2: Reconstroi o caminho do nó final até o nó inicial
    path = []
    current = end_node

    if distances[end_node] == float("infinity"):
        # Se o nó final não é alcançável
        return [], distances[end_node]

    while current is not None:
        path.append(current)
        current = predecessors[current]

    path.reverse()

    print(distances)

    return path, distances[end_node]


edges = [
    [0, 1, 2],
    [1, 2, 3],
    [1, 3, 1],
    [1, 4, 3],
    [2, 4, 2],
    [3, 6, 6],
    [3, 8, 3],
    [4, 6, 3],
    [4, 5, 2],
    [5, 6, 5],
    [6, 8, 4],
    [6, 7, 2],
    [7, 9, 7],
    [9, 8, 5],
]

graph = defaultdict(dict)
for first_node, second_node, weight in edges:
    graph[first_node][second_node] = weight

start_node = 0
end_node = 7

path, total_distance = dijkstra(graph, 0, 7)

print(path, total_distance)

print(" ".join(map(str, path)))
