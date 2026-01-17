def summary_ranges(nums: list[int]) -> list[int]:
    n = len(nums)
    ranges = list()
    if n == 0:
        return ranges

    start = nums[0]

    for index in range(n):
        num = nums[index]
        if index == n - 1 or num + 1 != nums[index + 1]:
            if start == num:
                ranges.append(f"{start}")
            else:
                ranges.append(f"{start}->{num}")

            if index < n - 1:
                start = nums[index + 1]

    return ranges
    # Time: O(n)
    # Space: O(n)


# print(summary_ranges([0, 1, 2, 4, 5, 7]))
# print(summary_ranges([0, 2, 3, 4, 6, 8, 9]))
print(summary_ranges([0, 0, 0, 0]))
