def rotate_array(nums: list[int], k: int):
    n = len(nums)
    k = k % n

    def reverse(nums, left: int, right: int):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1

    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)

    return nums


print(rotate_array([1, 2, 3, 4, 5], 2))
print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))
print(rotate_array([-1, -100, 3, 99], 2))
