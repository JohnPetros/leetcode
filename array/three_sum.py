def three_sum(numbers: list[int]) -> list[list[int]]:
    numbers.sort()
    sums = []

    for start in range(len(numbers)):
        if numbers[start] > 0:
            break

        if start > 0 and numbers[start] == numbers[start - 1]:
            continue

        left_pointer = start + 1
        right_pointer = len(numbers) - 1

        while left_pointer < right_pointer:
            combination = [
                numbers[start],
                numbers[left_pointer],
                numbers[right_pointer],
            ]

            current_sum = sum(combination)
            if current_sum == 0:
                sums.append(combination)
                left_pointer += 1
                right_pointer -= 1

                while (
                    left_pointer < right_pointer
                    and numbers[left_pointer] == numbers[left_pointer - 1]
                ):
                    left_pointer += 1
                while (
                    left_pointer < right_pointer
                    and numbers[right_pointer] == numbers[right_pointer + 1]
                ):
                    right_pointer -= 1
            elif current_sum < 0:
                left_pointer += 1
            else:
                right_pointer -= 1

    return sums


# print(three_sum([-3, -3, -2, -1, 0, 1, 2, 2, 3]))
# print(three_sum([-1, 0, 1, 2, -1, -4]))
# print(three_sum([0, 1, 1]))
# print(three_sum([2, 4, 1, 0, -3, -1]))
print(three_sum([0, 0, 0]))
# print(three_sum([-1, 0, 1, 2, -1, -4]))
