def remove_element(nums: list[int], val: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[left] != val:
            left += 1
        elif nums[right] == val:
            right -= 1
        else:
            nums[left] = nums[right]
            left += 1
            right -= 1

    return left
    # Time: O(N)
    # Space: O(1)


# print(remove_element([2, 3, 1, 2, 3, 2, 4], 2))
# print(remove_element([3, 2, 2, 3], 3))
# print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
print(remove_element([1], 1))
