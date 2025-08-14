from collections import defaultdict


def kosaraju(graph, all_nodes):
    # Passo 1: DFS para gerar pilha de finalização
    def dfs(v, visited, stack):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor, visited, stack)
        stack.append(v)

    visited = set()
    stack = []
    for node in all_nodes:
        if node not in visited:
            dfs(node, visited, stack)

    # Passo 2: Reverter o grafo
    reversed_graph = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            reversed_graph[v].append(u)

    # Passo 3: DFS no grafo invertido para achar SCCs
    def dfs_rev(v, visited, components):
        visited.add(v)
        components.append(v)
        for neighbor in reversed_graph[v]:
            if neighbor not in visited:
                dfs_rev(neighbor, visited, components)

    visited = set()
    sccs = []
    while stack:
        node = stack.pop()
        if node not in visited:
            components = []
            dfs_rev(node, visited, components)
            sccs.append(components)

    return sccs


# Exemplo de uso
edges = [
    [1, 2],
    [3, 2],
    [1, 3],
    [2, 3],
]
graph = defaultdict(list)
all_nodes = set()

for u, v in edges:
    graph[u].append(v)
    all_nodes.add(u)
    all_nodes.add(v)

print(kosaraju(graph, all_nodes))
