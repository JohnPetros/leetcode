def valid_soduku(soduku):
    for row in soduku:
        visited_elements = set()
        for element in row:
            if element != "." and element in visited_elements:
                return False

            visited_elements.add(element)

    for column in range(9):
        visited_elements = set()
        for row in range(9):
            element = soduku[row][column]
            if element != "." and element in visited_elements:
                return False

            visited_elements.add(element)

    for square_column in range(0, 9, 3):
        for square_row in range(0, 9, 3):
            visited_elements = set()
            for column in range(square_column, 3 + square_column):
                for row in range(square_row, 3 + square_row):
                    element = soduku[row][column]
                    if element != "." and element in visited_elements:
                        return False

                    visited_elements.add(element)

    return True


print(
    valid_soduku(
        [
            ["1", "2", ".", ".", "3", ".", ".", ".", "."],
            ["4", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", ".", "3"],
            ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
            [".", ".", ".", "8", ".", "3", ".", ".", "5"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "8"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
