def kosaraju(vertices_count: int, graph: dict[int], inverted_graph: dict[int]):
    visited = [False] * (vertices_count + 1)

    def dfs(index: int, graph: dict[list], visited: list[bool]) -> None:
        visited[index] = True

        for neighbor in graph[index]:
            if not visited[neighbor]:
                dfs(neighbor, graph, visited)

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
