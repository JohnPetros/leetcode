from collections import defaultdict, deque


def bfs(graph, start_node, end_node):
    queue = deque([(start_node, [start_node])])

    visited = set([start_node])

    while queue:
        current_node, path = queue.popleft()

        if current_node == end_node:
            return path

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))

    return None


inputs = [
    "Aldo Beto",
    "Aldo Drica",
    "Beto Cris",
    "Beto Ella",
    "Drica Ella",
    "Ella Fran",
    "Ella Gigi",
    "Isa Katy",
]

graph = defaultdict(list)

for input in inputs:
    student1, student2 = input.split()
    graph[student1].append(student2)
    graph[student2].append(student1)

connections = [
    "Aldo Beto",
    "Aldo Cris",
    "Aldo Drica",
    "Aldo Ella",
    "Aldo Fran",
    "Aldo Gigi",
    "Aldo Isa",
    "Aldo Katy",
    "Beto Aldo",
    "Beto Gigi",
    "Cris Aldo",
    "Cris Drica",
    "Cris Gigi",
    "Cris Isa",
    "Drica Fran",
    "Drica Katy",
    "Fran Aldo",
    "Fran Beto",
    "Gigi Aldo",
    "Isa Katy",
    "Katy Isa",
    "Isa Aldo",
    "Katy Gigi",
]

for connection in connections:
    student1, student2 = connection.split()
    path = bfs(graph, student1, student2)

    if path is None:
        print(f"{student1}-{student2} sem conexao")
    else:
        print(f"{student1}-{student2} {len(path) - 1}")
