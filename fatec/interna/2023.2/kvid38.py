from copy import deepcopy

TESTE = True


def kvid38(matrix: list[list[int]]):
    can_be_contamination = True

    while can_be_contamination:
        can_be_contamination = False
        new_matrix = deepcopy(matrix)
        for row in range(5):
            for column in range(5):
                top, bottom, left, right = None, None, None, None

                if row > 0:
                    top = matrix[row - 1][column]
                if row < 4:
                    bottom = matrix[row + 1][column]
                if column > 0:
                    left = matrix[row][column - 1]
                if column < 4:
                    right = matrix[row][column + 1]

                contaminated = [cell for cell in [top, bottom, left, right] if cell]

                if matrix[row][column] == 0 and len(contaminated) >= 2:
                    new_matrix[row][column] = 1
                    can_be_contamination = True

        matrix = new_matrix

    for row in matrix:
        print("".join(map(str, row)))


if TESTE:
    kvid38(
        [
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 1, 1],
            [0, 0, 1, 1, 1],
            [0, 1, 1, 1, 1],
        ]
    )
    kvid38(
        [
            [1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
        ]
    )
else:
    try:
        while True:
            matrix = []
            for _ in range(5):
                row = list(map(int, list(input())))
                matrix.append(row)
            kvid38(matrix)
    except EOFError:
        pass
