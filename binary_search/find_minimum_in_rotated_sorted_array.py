def find_minimum_in_rotated_sorted_array(array: list[int]) -> int:
    left_pointer = 0
    right_pointer = len(array) - 1

    while left_pointer < right_pointer:
        middle_pointer = (left_pointer + right_pointer) // 2

        if array[middle_pointer] > array[right_pointer]:
            left_pointer = middle_pointer + 1
        else:
            right_pointer = middle_pointer

    return array[left_pointer]
    # Time complexity: O(log n)
    # Space complexity: O(1)


print(find_minimum_in_rotated_sorted_array([3, 4, 5, 1, 2]))  # 1
