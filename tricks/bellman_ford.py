from collections import defaultdict


def bellman_ford(graph, start_node):
    # Passo 1: Inicializa as distâncias para todos os nós
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        all_nodes.update(neighbors.keys())

    distances = {node: float("infinity") for node in all_nodes}
    distances[start_node] = 0

    num_nodes = len(all_nodes)

    # Passo 2: Relaxa todas as arestas V - 1 vezes
    for i in range(num_nodes - 1):
        for first_node in graph:
            for second_node, weight in graph[first_node].items():
                if (
                    distances[first_node] != float("infinity")
                    and distances[first_node] + weight < distances[second_node]
                ):
                    distances[second_node] = distances[first_node] + weight

    # Passo 3: Verifica se há ciclos negativos
    for first_node in graph:
        for second_node, weight in graph[first_node].items():
            if (
                distances[first_node] != float("infinity")
                and distances[first_node] + weight < distances[second_node]
            ):
                return False  # Ciclo negativo detectado

    return distances


edges = [
    [0, 1, 5],
    [0, 2, 4],
    [1, 3, 3],
    [2, 1, -6],  # Aresta negativa
    [3, 2, 2],
]

graph = defaultdict(dict)
all_nodes = set()
for u, v, w in edges:
    graph[u][v] = w
    all_nodes.add(u)
    all_nodes.add(v)
for node in all_nodes:
    if node not in graph:
        graph[node] = {}


start_node = 0
shortest_paths = bellman_ford(graph, start_node)

print(shortest_paths)

if shortest_paths:
    print(f"Distâncias a partir de '{start_node}': {shortest_paths}")
