from collections import deque


def bfs_shortest_path_in_maze(maze, start, target):
    rows_count = len(maze)
    columns_count = len(maze[0])

    # A fila agora armazena tuplas: (coordenadas, caminho_ate_aqui)
    # Coordenadas são (linha, coluna)
    queue = deque([(start, [start])])

    # O conjunto de visitados armazena as tuplas de coordenadas
    visited = {start}

    while queue:
        (current_row, current_column), path = queue.popleft()

        # Se as coordenadas atuais são o destino, encontramos o caminho
        if (current_row, current_column) == target:
            return path

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
                        novo_caminho = path + [(next_row, next_column)]
                        queue.append(((next_row, next_column), novo_caminho))

    # Se a fila esvaziar, não há caminho
    return None


# O labirinto de Exemplo
maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
]

# ATENÇÃO: O problema usa coordenadas base 1, Python usa base 0.
# Então, subtraímos 1 de cada coordenada.
start = (10 - 1, 6 - 1)  # (9, 5)
end = (2 - 1, 10 - 1)  # (1, 9)

shortest_path = bfs_shortest_path_in_maze(maze, start, end)

print(shortest_path)

if shortest_path:
    print("Caminho mais curto encontrado:")
    for row, column in shortest_path:
        print(f"{row + 1} {column + 1}")
else:
    print("Não foi possível encontrar um caminho.")
