def alphabetic_layers(layers_count: int) -> None:
    matrix_order = 3 + (layers_count - 1) * 2

    matrix = [[0] * matrix_order for _ in range(matrix_order)]

    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    character_index = 0
    characters_count = 1
    max_characters_count = matrix_order**2

    first_row = 0
    last_row = matrix_order - 1
    first_column = 0
    last_column = matrix_order - 1

    while characters_count <= max_characters_count:
        if characters_count == max_characters_count:
            character = "*"
        else:
            character = characters[character_index]

        for column in range(first_column, last_column + 1):
            matrix[first_row][column] = character
            characters_count += 1
        first_row += 1

        for row in range(first_row, last_row + 1):
            matrix[row][last_column] = character
            characters_count += 1
        last_column -= 1

        for column in range(last_column, first_column - 1, -1):
            matrix[last_row][column] = character
            characters_count += 1
        last_row -= 1

        for row in range(last_row, first_row - 1, -1):
            matrix[row][first_column] = character
            characters_count += 1
        first_column += 1

        character_index += 1

    for row in matrix:
        for column in row:
            print(column, end=" ")
        print("")


alphabetic_layers(int(input("Valor de N: ")))
