def valid_sodoku(board: list[list[str]]) -> list[list[str]]:
    for row in board:
        empty_cells_count = row.count(".")
        is_valid_row = (len(set(row)) + empty_cells_count - 1) == 9
        if not is_valid_row:
            return False

    for column in range(9):
        column_elements = list()
        for row in board:
            column_elements.append(row[column])

        empty_cells_count = column_elements.count(".")
        is_valid_row = (len(set(column_elements)) + empty_cells_count - 1) == 9
        if not is_valid_row:
            return False

    for square_y in range(0, 9, 3):
        for square_x in range(0, 9, 3):
            square_elements = list()
            for column in range(square_x, square_x + 3):
                for row in range(square_y, square_y + 3):
                    square_elements.append(board[row][column])

            empty_cells_count = square_elements.count(".")
            is_valid_row = (len(set(square_elements)) + empty_cells_count - 1) == 9
            if not is_valid_row:
                return False

    return True


print(
    valid_sodoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
