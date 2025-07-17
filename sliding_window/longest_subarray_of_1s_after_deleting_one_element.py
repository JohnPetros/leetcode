def longest_subarray_of_1s_after_deleting_one_element(numbers: list[int]) -> int:
    start = 0
    window = 0
    zeros_count = 0
    longest_window = 0

    for end in range(len(numbers)):
        if numbers[end] == 1:
            window = end - start + 1
            longest_window = max(longest_window, window)
        else:
            zeros_count += 1

        while zeros_count == 2:
            if numbers[start] == 0:
                zeros_count -= 1
            start += 1

    return longest_window - 1


print(longest_subarray_of_1s_after_deleting_one_element([1, 1, 0, 1]))
print(longest_subarray_of_1s_after_deleting_one_element([0, 1, 1, 1, 0, 1, 1, 0, 1]))
print(longest_subarray_of_1s_after_deleting_one_element([1, 1, 1]))
