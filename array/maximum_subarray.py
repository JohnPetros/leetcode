def maximum_subarray(numbers: list[int]) -> int:
    maximum_sum = float("-inf")
    current_sum = 0

    for number in numbers:
        current_sum = max(number, current_sum + number)

        if current_sum > maximum_sum:
            maximum_sum = current_sum

    return maximum_sum


# print(maximum_subarray([1, 8, -4, 3, 7, 2, -5]))
print(maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
