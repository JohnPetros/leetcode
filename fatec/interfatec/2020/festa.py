from collections import defaultdict, deque


def bfs_is_bipartite_graph(graph, node, sets):
    queue = deque([(node, "U")])
    sets[node] = "U"

    while queue:
        current_node, current_set = queue.popleft()
        opposite_set = "V" if current_set == "U" else "U"

        for neighbor in graph[current_node]:
            if neighbor not in sets:
                sets[neighbor] = opposite_set
                queue.append((neighbor, opposite_set))
            # Esta é a checagem de conflito!
            elif sets[neighbor] == current_set:
                return False  # Conflito: estão no mesmo ambiente

    return True  # Nenhum conflito encontrado neste componente


edges = [
    [1, 2],
    [1, 3],
    [1, 4],
    [2, 3],
]
graph = defaultdict(list)
all_nodes = set()
for first_node_, second_node in edges:
    graph[first_node_].append(second_node)
    graph[second_node].append(first_node_)
    all_nodes.add(first_node_)
    all_nodes.add(second_node)


# Lógica principal que lida com grafos desconectados
sets = dict()
is_bipartite = True

for node in all_nodes:
    if node not in sets:
        if not bfs_is_bipartite_graph(graph, node, sets):
            is_bipartite = False
            break

print("FESTA!" if is_bipartite else "Lascou...")
