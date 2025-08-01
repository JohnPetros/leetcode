from collections import defaultdict

UNVISITED = 0
VISITING = 1
VISITED = 2


def dfs_detect_cycle_in_graph(graph, node, states):
    state = states[node]

    if state == VISITING:
        return True
    if state == VISITED:
        return False

    states[node] = VISITING

    for neighbor in graph[node]:
        if dfs_detect_cycle_in_graph(graph, neighbor, states):
            return True

    states[node] = VISITED

    return False


edges = [
    ["A", "B"],
    ["B", "C"],
    ["C", "A"],
]

graph = defaultdict(list)
all_nodes = []

for first_node, second_node in edges:
    graph[first_node].append(second_node)
    all_nodes.append(first_node)
    all_nodes.append(second_node)

states = {node: UNVISITED for node in all_nodes}
