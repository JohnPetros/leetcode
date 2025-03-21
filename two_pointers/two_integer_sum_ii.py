def two_sum_ii_sorted_array(numbers: list[int], target: int) -> list[int, int]:
    left_pointer = 0
    right_pointer = len(numbers) - 1

    while left_pointer < right_pointer:
        sum = numbers[left_pointer] + numbers[right_pointer]
        if sum > target:
            right_pointer -= 1
        elif sum < target:
            left_pointer += 1
        else:
            return [left_pointer + 1, right_pointer + 1]


print(two_sum_ii_sorted_array([1, 2, 3, 4], 3))
print(two_sum_ii_sorted_array([1, 2, 3, 4], 3))
