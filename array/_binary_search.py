def binary_search(
    numbers: list[int], target: int, start_index: int = 0, end_index: int = -1
) -> int:
    if end_index == -1:
        end_index = len(numbers) - 1

    if start_index <= end_index:
        half_index = (start_index + end_index) // 2

        if numbers[half_index] == target:
            return half_index

        if target < numbers[half_index]:
            return binary_search(numbers, target, start_index, half_index - 1)

        return binary_search(numbers, target, half_index + 1, end_index)

    return -1


print(binary_search([2, 3, 4], 3))
