def remove_duplicates_from_sorted_array_ii(nums: list[int]):
    j = 1
    count = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1
        else:
            count = 1

        if count <= 2 and nums[i] != nums[j]:
            nums[j] = nums[i]
            j += 1
        elif count <= 2:
            j += 1

    return nums, j


print(remove_duplicates_from_sorted_array_ii([0, 0, 0, 0, 1, 2, 2, 2, 3]))
