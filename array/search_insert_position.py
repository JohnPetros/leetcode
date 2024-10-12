def search_insert_position(numbers: list[int], target: int) -> list[int]:
    left_pointer = 0
    right_pointer = len(numbers) - 1

    while left_pointer <= right_pointer:
        middle_pointer = left_pointer + (right_pointer - left_pointer) // 2

        if numbers[middle_pointer] == target:
            return middle_pointer

        if numbers[middle_pointer] < target:
            left_pointer = middle_pointer + 1
            continue

        right_pointer = middle_pointer - 1

    return left_pointer


print(search_insert_position([1, 2, 3, 4, 6, 7, 8], 5))
