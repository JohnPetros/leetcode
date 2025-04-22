def binary_search(numbers: list[int], target: int) -> int:
    left_pointer = 0
    right_pointer = len(numbers) - 1

    while left_pointer <= right_pointer:
        middle_pointer = (left_pointer + right_pointer) // 2

        if numbers[middle_pointer] == target:
            return middle_pointer
        elif numbers[middle_pointer] < target:
            left_pointer = middle_pointer + 1
        else:
            right_pointer = middle_pointer - 1

    return -1
    # Time complexity: O(log n)
    # Space complexity: O(1)


print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([-1, 0, 3, 5, 9, 12], 9))
print(binary_search([-1, 0, 3, 5, 9, 12], 2))
