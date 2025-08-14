from collections import deque


def bfs_shortest_path_adjacency_graph(graph, start_node, end_node):
    # Fila para armazenar tuplas (nó_atual, caminho_ate_aqui)
    # Cada elemento na fila é uma tupla: (nó, [lista_de_nós_no_caminho])
    queue = deque([(start_node, [start_node])])

    # Conjunto para armazenar os nós já visitados
    visited = set([start_node])

    while queue:
        current_node, path = queue.popleft()

        # Se o nó atual é o destino, encontramos o caminho mais curto!
        if current_node == end_node:
            return path

        # Explora os vizinhos do nó atual
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                # Cria um novo caminho estendendo o caminho atual com o vizinho
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))

    # Se a fila esvaziar e o nó final não for encontrado, não há caminho
    return None


# Nosso grafo de exemplo
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

# Encontrar o caminho mais curto de 'A' para 'F'
path_A_to_F = bfs_shortest_path_adjacency_graph(graph, "A", "F")
if path_A_to_F:
    print(f"Caminho mais curto de 'A' para 'F': {path_A_to_F}")
else:
    print("Não foi possível encontrar um caminho de 'A' para 'F'.")

# Encontrar o caminho mais curto de 'A' para 'D'
path_A_to_D = bfs_shortest_path_adjacency_graph(graph, "A", "D")
if path_A_to_D:
    print(f"Caminho mais curto de 'A' para 'D': {path_A_to_D}")
else:
    print("Não foi possível encontrar um caminho de 'A' para 'D'.")

# Exemplo de caminho que não existe (se o grafo fosse diferente)
# path_A_to_Z = bfs(graph, 'A', 'Z')
# if path_A_to_Z:
#     print(f"Caminho mais curto de 'A' para 'Z': {path_A_to_Z}")
# else:
#     print("Não foi possível encontrar um caminho de 'A' para 'Z'.")
