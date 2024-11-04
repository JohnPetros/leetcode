def rotate_image(matrix: list[list[int]]) -> list[int]:
    lines = columns = len(matrix)

    for line in range(lines):
        for column in range(line + 1, columns):
            matrix[line][column], matrix[column][line] = (
                matrix[column][line],
                matrix[line][column],
            )

    for line in range(lines):
        for column in range(lines // 2):
            matrix[line][column], matrix[line][lines - column - 1] = (
                matrix[line][lines - column - 1],
                matrix[line][column],
            )

    return matrix


print(rotate_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# 1 2 3 4 5
