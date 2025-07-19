def dfs(index: int, graph: dict[list], visited: list[bool]) -> None:
    visited[index] = True

    for neighbor in graph[index]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited)


def kosaraju(vertices_count: int, graph: dict[int], inverted_graph: dict[int]):
    visited = [False] * (vertices_count + 1)

    dfs(1, graph, visited)

    for index in range(1, vertices_count + 1):
        if not visited[index]:
            return False

    visited = [False] * (vertices_count + 1)

    dfs(1, inverted_graph, visited)

    for index in range(1, vertices_count + 1):
        if not visited[index]:
            return False

    return True


while True:
    try:
        vertices_count, edges_count = map(int, input().split())

        graph = {index: [] for index in range(1, vertices_count + 1)}
        inverted_graph = {index: [] for index in range(1, vertices_count + 1)}

        if vertices_count == 0 and edges_count == 0:
            break

        for _ in range(edges_count):
            vertice1, vertice2, connection = map(int, input().split())

            graph[vertice1].append(vertice2)
            inverted_graph[vertice2].append(vertice1)

            if connection == 2:
                graph[vertice2].append(vertice1)
                inverted_graph[vertice1].append(vertice2)

        if kosaraju(vertices_count, graph, inverted_graph):
            print("S")
        else:
            print("N")
    except EOFError:
        break
