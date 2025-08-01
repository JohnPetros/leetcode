rows, columns = "25 25".split()
target = "24 24".split()

rows = int(rows)
columns = int(columns)
last_row = rows - 1
last_column = columns - 1

matrix = [[0] * columns for _ in range(rows)]

for row in range(rows):
    for column in range(columns):
        if row == 0:
            matrix[row][column] = 0
        elif column == last_column:
            matrix[row][column] = 1
        elif row == last_row:
            matrix[row][column] = 2
        elif column == 0:
            matrix[row][column] = 3
        else:
            numbers = [
                matrix[row][column - 1],
                matrix[row - 1][column],
                matrix[row - 1][column - 1],
            ]
            number = sum(numbers)
            matrix[row][column] = number


print(matrix[int(target[0]) - 1][int(target[1]) - 1])
