def spiral_matrix(matrix: list[list[int]]) -> list[int]:
    spiral = []

    while matrix:
        spiral += matrix.pop(0)

        if matrix and matrix[0]:
            for row in matrix:
                spiral.append(row.pop())

        if matrix:
            spiral += matrix.pop()[::-1]

        if matrix and matrix[0]:
            for row in matrix[::-1]:
                spiral.append(row.pop(0))

    return spiral


# print(spiral_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiral_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
