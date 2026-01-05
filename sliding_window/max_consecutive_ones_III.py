def max_consecutive_ones_III(nums: list[int], k: int) -> int:
    left = max_consecutive = zero_count = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        window = right - left + 1
        max_consecutive = max(window, max_consecutive)

    return max_consecutive


# print(max_consecutive_ones_III([1, 1, 1, 0, 0, 0, 1, 1, 1, 1], 2))
print(
    max_consecutive_ones_III(
        [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3
    )
)
