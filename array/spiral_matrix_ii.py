def spiral_matrix_ii(matrix_order: int) -> list[list[int]]:
    matrix = [[0] * matrix_order for _ in range(matrix_order)]

    number = 1

    first_row = 0
    last_row = matrix_order - 1
    first_column = 0
    last_column = matrix_order - 1

    while number <= matrix_order * matrix_order:
        for column in range(first_column, last_column + 1):
            matrix[first_row][column] = number
            number += 1
        first_row += 1

        for row in range(first_row, last_row + 1):
            matrix[row][last_column] = number
            number += 1
        last_column -= 1

        for column in range(last_column, first_column - 1, -1):
            matrix[last_row][column] = number
            number += 1
        last_row -= 1

        for row in range(last_row, first_row - 1, -1):
            matrix[row][first_column] = number
            number += 1
        first_column += 1

    return matrix


print(spiral_matrix_ii(3))
