def minimum_size_subarray_sum(target: int, nums: list[int]) -> int:
    min_length = float("inf")
    n = len(nums)
    left = 0
    right = 0
    sum = 0

    for right in range(n):
        sum += nums[right]

        while sum >= target:
            window = right - left + 1
            min_length = min(window, min_length)
            sum -= nums[left]
            left += 1

    if min_length == float("inf"):
        return 0

    return min_length
    # Time: O(n)
    # Space: O(1)


print(minimum_size_subarray_sum(7, [2, 3, 1, 2, 4, 3]))
# print(minimum_size_subarray_sum(4, [1, 4, 4]))
