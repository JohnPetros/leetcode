def search_in_rotated_sorted_array(
    numbers: list[int], target: int, left_pointer: int = 0, right_pointer: int = -1
) -> int:
    if right_pointer == -1:
        right_pointer = len(numbers) - 1

    while left_pointer <= right_pointer:
        mid_pointer = (left_pointer + right_pointer) // 2

        if numbers[mid_pointer] == target:
            return mid_pointer

        if numbers[left_pointer] <= numbers[mid_pointer]:
            if numbers[left_pointer] <= target < numbers[mid_pointer]:
                return search_in_rotated_sorted_array(
                    numbers, target, left_pointer, mid_pointer - 1
                )
            return search_in_rotated_sorted_array(
                numbers, target, mid_pointer + 1, right_pointer
            )

        if numbers[mid_pointer] < target <= numbers[right_pointer]:
            return search_in_rotated_sorted_array(
                numbers, target, mid_pointer + 1, right_pointer
            )

        return search_in_rotated_sorted_array(
            numbers, target, left_pointer, mid_pointer - 1
        )

    return -1


print(search_in_rotated_sorted_array([3, 4, 5, 0, 1, 2], 4))
