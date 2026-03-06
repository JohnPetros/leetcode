def concatenation_of_array(nums: list[int]) -> list[int]:
    output = nums.copy()

    for num in nums:
        output.append(num)

    return output
    # Time: O(N)
    # Space: O(N)


print(concatenation_of_array([1, 2]))
print(concatenation_of_array([1, 3, 2, 1]))
