def maximum_average_subarray_i(nums: list[int], k: int) -> float:
    current_sum = 0

    for index in range(k):
        current_sum += nums[index]

    maximum_average = current_sum / k

    for index in range(k, len(nums)):
        current_sum += nums[index]
        current_sum -= nums[index - k]
        maximum_average = max(current_sum / k, maximum_average)

    return maximum_average
    # Time: O(n)
    # Space: O(1)


# print(maximum_average_subarray_i([1, 12, -5, -6, 50, 3], 4))
# print(maximum_average_subarray_i([1, 2, 3, 4], 5))
# print(maximum_average_subarray_i([5], 1))
print(maximum_average_subarray_i([7, 4, 5, 8, 8, 3, 9, 8, 7, 6], 7))
