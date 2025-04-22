def search_a_2d_matrix(matrix: list[list[int]], target: int) -> bool:
    left_pointer = 0
    right_pointer = len(matrix) - 1

    if right_pointer == -1:
        return False

    def search_row(row: list[int]):
        left_pointer = 0
        right_pointer = len(row) - 1

        while left_pointer <= right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2

            if row[middle_pointer] == target:
                return True
            elif row[middle_pointer] < target:
                left_pointer = middle_pointer + 1
            else:
                right_pointer = middle_pointer - 1

        return False

    while left_pointer <= right_pointer:
        middle_pointer = (left_pointer + right_pointer) // 2
        middle_row = matrix[middle_pointer]

        is_found = search_row(middle_row)
        if is_found:
            return True
        elif middle_row[0] < target:
            left_pointer = middle_pointer + 1
        else:
            right_pointer = middle_pointer - 1

    return False


print(search_a_2d_matrix([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 18))  # True
