def find_the_difference_of_two_arrays(
    nums1: list[int], nums2: list[int]
) -> list[list[int]]:
    nums1_set = set(nums1)
    nums2_set = set(nums2)

    difference1 = []
    difference2 = []

    for num in nums1_set:
        if num not in nums2_set:
            difference1.append(num)

    for num in nums2_set:
        if num not in nums1_set:
            difference2.append(num)

    return [difference1, difference2]
    # Time: O(N + M)
    # Space: O(N + M)


print(find_the_difference_of_two_arrays([1, 2, 3], [2, 4, 6]))
