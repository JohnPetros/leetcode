from collections import defaultdict


def tarjan(graph, all_nodes):
    index = 0
    stack = []
    on_stack = set()
    indexes = {}
    lowlinks = {}
    sccs = []

    def strongconnect(v):
        nonlocal index
        indexes[v] = index
        lowlinks[v] = index
        index += 1
        stack.append(v)
        on_stack.add(v)

        for w in graph[v]:
            if w not in indexes:
                strongconnect(w)
                lowlinks[v] = min(lowlinks[v], lowlinks[w])
            elif w in on_stack:
                lowlinks[v] = min(lowlinks[v], indexes[w])

        if lowlinks[v] == indexes[v]:
            comp = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                comp.append(w)
                if w == v:
                    break
            sccs.append(comp)

    for v in all_nodes:
        if v not in indexes:
            strongconnect(v)

    return sccs


# Exemplo
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

print(tarjan(graph, all_nodes))
