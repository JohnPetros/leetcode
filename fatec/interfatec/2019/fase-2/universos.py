from collections import defaultdict


def tarjan(graph):
    time = 0
    stack = []
    on_stack = set()
    dfs_num = {}
    dfs_low = {}
    sccs = []

    def dfs(v):
        nonlocal time
        dfs_num[v] = dfs_low[v] = time
        time += 1

        stack.append(v)
        on_stack.add(v)

        for u in graph[v]:
            if u not in dfs_num:
                dfs(u)
                dfs_low[v] = min(dfs_low[v], dfs_low[u])
            elif u in on_stack:
                dfs_low[v] = min(dfs_low[v], dfs_num[u])

        if dfs_low[v] == dfs_num[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)

    for node in graph:
        if node not in dfs_num:
            dfs(node)

    return sccs


def kosajaru(): ...


edges = [
    [1, 2],
    [3, 2],
    [1, 3],
    [2, 3],
]

graph = defaultdict(list)
nodes = set()

for first_node, second_node in edges:
    graph[first_node].append(second_node)
    nodes.add(first_node)
    nodes.add(second_node)

# Para garantir que todos os nós estejam no grafo, mesmo os que não têm arestas de saída.
for node in nodes:
    if node not in graph:
        graph[node] = []


# Executa o algoritmo e imprime o resultado
sccs = tarjan(graph)

print("S" if len(sccs) == 1 else "N")
