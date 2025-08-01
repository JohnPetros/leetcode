from collections import deque


# A sua função está correta, não precisa de alterações.
def bfs_shortest_path_in_maze(maze, start, target):
    """
    Encontra o caminho mais curto em um labirinto (grid graph) usando BFS.

    :param maze: Uma lista de listas (matriz) representando o grid. 1 é caminho, 0 é parede.
    :param start: Uma tupla (linha, coluna) para o ponto de partida.
    :param target: Uma tupla (linha, coluna) para o ponto de destino.
    :return: Uma lista de tuplas representando o caminho, ou None se não houver caminho.
    """
    rows_count = len(maze)
    columns_count = len(maze[0])

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (current_row, current_column), path = queue.popleft()

        if (current_row, current_column) == target:
            return path

        movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for row, column in movements:
            next_row, next_column = current_row + row, current_column + column

            if 0 <= next_row < rows_count and 0 <= next_column < columns_count:
                # A lógica de verificação usa o valor 1 para uma passagem válida
                if maze[next_row][next_column] == 1:
                    if (next_row, next_column) not in visited:
                        visited.add((next_row, next_column))
                        new_path = path + [(next_row, next_column)]
                        queue.append(((next_row, next_column), new_path))
    return None


# --- Dados de Entrada ---
input_string = """0000000000
1100011111
0110010000
0011110000
0010011110
1110000010
0011110000
0000011111
0000010000
0000010000"""
start_str = "10 6"
target_str = "2 10"

# --- Preparação dos Dados ---
maze = []
for row_str in input_string.strip().split("\n"):
    row_int = [int(char) for char in row_str]
    maze.append(row_int)

# CORREÇÃO: Converter coordenadas de base 1 (problema) para base 0 (Python)
start_coords = tuple(coord - 1 for coord in map(int, start_str.split()))
target_coords = tuple(coord - 1 for coord in map(int, target_str.split()))

# --- Execução ---
path = bfs_shortest_path_in_maze(maze, start_coords, target_coords)

# Impressão do resultado (opcional: converter de volta para base 1 para visualização)
if path:
    print("Caminho encontrado (em coordenadas base 1):")
    for row, column in path:
        print(f"{row + 1} {column + 1}")
else:
    print("Não foi encontrado um caminho.")
