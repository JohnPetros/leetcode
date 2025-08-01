from pprint import pprint

width = 12
height = 19
commands = [
    (2, 4, 1),
    (6, 6, 1),
    (5, 5, 1),
    (6, 6, 2),
    (1, 5, 1),
    (2, 4, 2),
    (1, 6, 2),
]


matrix = [[0 for _ in range(width)] for _ in range(height)]
rows_count = len(matrix)


def run():
    max_height = 1

    for command in commands:
        start, end, material = command
        for column in range(start - 1, end):
            row = 0
            column_material = material
            while column_material != 0:
                while row < rows_count and matrix[row][column] == 1:
                    row += 1
                    max_height = max(row + 1, max_height)

                if row > rows_count:
                    return None

                matrix[row][column] = 1
                column_material -= 1

    return max_height


max_height = run()

if max_height is None:
    print("invalida")
else:
    print(max_height)
