from pprint import pprint
from copy import deepcopy

rows = 5
columns = 5
initial_matrix = [
    "00000",
    "00111",
    "01110",
    "00000",
    "00000",
]
target_time = 1

matrix = [[int(column) for column in row] for row in initial_matrix]


def count_neighbors(row, column, matrix):
    neighbor_count = 0

    if row > 0 and matrix[row - 1][column]:
        neighbor_count += 1

    if row < rows - 1 and matrix[row + 1][column]:
        neighbor_count += 1

    if column > 0 and matrix[row][column - 1]:
        neighbor_count += 1

    if column < columns - 1 and matrix[row][column + 1]:
        neighbor_count += 1

    if row > 0 and column > 0 and matrix[row - 1][column - 1]:
        neighbor_count += 1

    if row > 0 and column < columns - 1 and matrix[row - 1][column + 1]:
        neighbor_count += 1

    if row < rows - 1 and column > 0 and matrix[row + 1][column - 1]:
        neighbor_count += 1

    if row < rows - 1 and column < columns - 1 and matrix[row + 1][column + 1]:
        neighbor_count += 1

    return neighbor_count


for time in range(target_time):
    dead_cells = []
    alive_cells = []
    matrix_snapshot = deepcopy(matrix)

    for row in range(rows):
        for column in range(columns):
            neighbor_count = count_neighbors(row, column, matrix_snapshot)
            cell = matrix[row][column]

            if row == 2 and column == 1:
                print(matrix[row][column])
                print(neighbor_count)

            if cell and (neighbor_count < 2 or neighbor_count > 3):
                dead_cells.append((row, column))
            elif not cell and neighbor_count == 3:
                alive_cells.append((row, column))

    for row, column in dead_cells:
        matrix[row][column] = 0

    for row, column in alive_cells:
        matrix[row][column] = 1

pprint(matrix)
