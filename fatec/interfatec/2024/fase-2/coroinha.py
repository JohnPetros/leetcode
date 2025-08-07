rows, columns, movement_count, target_row, target_column = list(map(int, "".split()))
wind_movements = "DDDDD"

wind_movements_reverse = {
    "C": "B",
    "B": "C",
    "E": "D",
    "D": "E",
}

wind_movements = "".join([wind_movements_reverse[char] for char in wind_movements])

movements = {
    "C": (-1, 0),
    "B": (1, 0),
    "E": (0, -1),
    "D": (0, 1),
}

origin = [target_row, target_column]

matrix = [[0] * columns for _ in range(rows)]
matrix[target_row - 1][target_row - 1] = 1

for movement in wind_movements:
    row, column = movements[movement]
    next_row = origin[0] + row
    next_column = origin[1] + column

    if 0 <= next_row <= rows and 0 <= next_column <= columns:
        origin[0], origin[1] = next_row, next_column
    else:
        origin[0], origin[1] = -1, -1


print(f"{origin[0]} {origin[1]}")
