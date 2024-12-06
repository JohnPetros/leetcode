def k_vid_38(matrix):
    def check_cell_sides(row: int, column: int):
        neighbors = []

        if row - 1 >= 0:
            neighbors.append(matrix[row - 1][column])

        if row + 1 <= 4:
            neighbors.append(matrix[row + 1][column])

        if column - 1 >= 0:
            neighbors.append(matrix[row][column - 1])

        if column + 1 <= 4:
            neighbors.append(matrix[row][column + 1])

        if neighbors.count(1) >= 2:
            matrix[row][column] = 1
            return True

    while True:
        has_change = False
        for row in range(5):
            for column in range(5):
                if matrix[row][column] == 0:
                    is_cell_contaminated = check_cell_sides(row, column)
                    if is_cell_contaminated:
                        has_change = True

        if not has_change:
            break

    print(matrix)


# matrix = []

# for _ in range(5):
#     columns = input().split()
#     matrix.append(list(map(int, columns)))


# k_vid_38(matrix)

# k_vid_38(
#     [
#         [0, 0, 0, 0, 1],
#         [0, 0, 0, 0, 1],
#         [0, 0, 0, 1, 1],
#         [0, 0, 1, 1, 1],
#         [0, 1, 1, 1, 1],
#     ]
# )

k_vid_38(
    [
        [1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
    ]
)
