def three_sum_closest(numbers: list[int], target: int) -> int:
    numbers.sort()
    closest_sum = float("inf")

    for start in range(len(numbers) - 2):
        if start > 0 and numbers[start] == numbers[start - 1]:
            continue

        left_pointer = start + 1
        right_pointer = len(numbers) - 1
        while left_pointer < right_pointer:
            current_sum = (
                numbers[start] + numbers[left_pointer] + numbers[right_pointer]
            )

            if current_sum == target:
                return current_sum

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if current_sum > target:
                right_pointer -= 1
            elif current_sum < target:
                left_pointer += 1

    return closest_sum


print(three_sum_closest([-1, 2, 1, -4], 1))
print(three_sum_closest([0, 0, 0], 1))
