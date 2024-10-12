def find_first_and_last_position_of_element_in_sorted_array(
    numbers: list[int], target: int
) -> list[int]:

    def find_leftmost_target():
        left_pointer = 0
        right_pointer = len(numbers) - 1

        while left_pointer <= right_pointer:
            middle_pointer = left_pointer + (right_pointer - left_pointer) // 2

            if numbers[middle_pointer] == target:
                right_pointer = middle_pointer - 1
            elif numbers[middle_pointer] < target:
                left_pointer = middle_pointer + 1
            else:
                right_pointer = middle_pointer - 1

        return left_pointer

    def find_rightmost_target():
        left_pointer = 0
        right_pointer = len(numbers) - 1

        while left_pointer <= right_pointer:
            middle_pointer = left_pointer + (right_pointer - left_pointer) // 2

            if numbers[middle_pointer] == target:
                left_pointer = middle_pointer + 1
            elif numbers[middle_pointer] < target:
                left_pointer = middle_pointer + 1
            else:
                right_pointer = middle_pointer - 1

        return right_pointer

    leftmost_target = find_leftmost_target()
    rightmost_target = find_rightmost_target()

    if leftmost_target <= rightmost_target:
        return [leftmost_target, rightmost_target]

    return [-1, -1]


print(find_first_and_last_position_of_element_in_sorted_array([2, 4, 6, 6, 7, 8, 9], 6))
