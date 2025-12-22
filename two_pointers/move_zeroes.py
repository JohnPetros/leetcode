def move_zeroes(nums: list[int]) -> list[int]:
    left = 0
    right = 1
    n = len(nums)

    while left < right and left < n and right < n:
        while right < n and left < n and nums[left] != 0 and nums[right] != 0:
            right += 1
            left += 1

        while right < n and nums[right] == 0:
            right += 1

        while left < n and nums[left] != 0:
            left += 1

        if right < n and left < n and nums[left] == 0 and nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1

    return nums
    # Time: O(N)
    # Space: O(1)


# print(move_zeroes([0, 1, 0, 3, 12]))
# print(move_zeroes([0]))
# print(move_zeroes([4, 2, 4, 0, 0, 3, 0, 5, 1, 0]))
