def find_pivot_index(nums: list[int]) -> int:
    total_sum = sum(nums)
    prefix_sum = 0

    for index in range(len(nums)):
        current_sum = prefix_sum + nums[index]
        if total_sum - current_sum == prefix_sum:
            return index
        prefix_sum = current_sum

    return -1
    # Time: O(N)
    # Space: O(1)


# print(find_pivot_index([1, 7, 3, 6, 5, 6]))
# print(find_pivot_index([1, 2, 3]))
# print(find_pivot_index([2, 1, -1]))
