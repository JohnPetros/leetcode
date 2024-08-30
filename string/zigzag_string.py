def zigzag_string(string: str, rows_count: int) -> str:
    if rows_count == 1:
        return string

    zigzag = ""
    column = 0
    increment = 1

    rows = [[] for _ in range(rows_count)]

    for char in string:
        rows[column].append(char)
        if column == 0:
            increment = 1
        elif column == rows_count - 1:
            increment = -1

        column += increment

    for index in range(len(rows)):
        zigzag += "".join(rows[index])
    return zigzag


print(zigzag_string("paypalishiring", 3))
