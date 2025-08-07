from collections import deque


def bfs_shortest_path_in_maze(maze, start, target):
    """
    Encontra o caminho mais curto em um labirinto (grid graph) usando BFS.

    :param maze: Uma lista de listas (matriz) representando o grid. 1 é caminho, 0 é parede.
    :param start: Uma tupla (linha, coluna) para o ponto de partida.
    :param target: Uma tupla (linha, coluna) para o ponto de destino.
    :return: Uma lista de tuplas representando o caminho, ou None se não houver caminho.
    """
    # Dimensões do labirinto
    rows_count = len(maze)
    columns_count = len(maze[0])

    # A fila agora armazena tuplas: (coordenadas, caminho_ate_aqui)
    # Coordenadas são (linha, coluna)
    queue = deque([(start, 0)])

    # O conjunto de visitados armazena as tuplas de coordenadas
    visited = {start}

    while queue:
        (current_row, current_column), distance = queue.popleft()

        # Se as coordenadas atuais são o destino, encontramos o caminho
        if (current_row, current_column) == target:
            return distance

        # Movimentos possíveis: Cima, Baixo, Esquerda, Direita
        movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for row, column in movements:
            next_row, next_column = current_row + row, current_column + column

            # Valida o vizinho
            # 1. Está dentro dos limites do labirinto?
            if 0 <= next_row < rows_count and 0 <= next_column < columns_count:
                # 2. Não é uma parede (deve ser um caminho válido)?
                if maze[next_row][next_column] == 1:
                    # 3. Ainda não foi visitado?
                    if (next_row, next_column) not in visited:
                        # Se o vizinho é válido, adiciona à fila e marca como visitado
                        visited.add((next_row, next_column))
                        queue.append(((next_row, next_column), distance + 1))

    # Se a fila esvaziar, não há caminho
    return -1


maze = [[1] * 100 for _ in range(100)]

start = (50, 50)
target = (0, 99)
obstacles = [
    (10, 10),
    (20, 20),
    (30, 30),
    (40, 40),
    (60, 60),
]

for row, column in obstacles:
    maze[row - 1][column - 1] = 0

shortest_path = bfs_shortest_path_in_maze(maze, start, target)

print(shortest_path)
