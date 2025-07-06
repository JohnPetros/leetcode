def contains_duplicate_ii(numbers, k):
    window = set()
    left_pointer = 0

    for right_pointer in range(len(numbers)):
        if right_pointer - left_pointer > k:
            window.remove(numbers[left_pointer])
            left_pointer += 1

        if numbers[right_pointer] in window:
            return True

        window.add(numbers[right_pointer])

    return False
    # Time complexity: O(n)
    # Space complexity: O(n)


print(contains_duplicate_ii([1, 2, 3, 1], 3))  # True
print(contains_duplicate_ii([1, 0, 1, 1], 1))  # True
print(contains_duplicate_ii([1, 2, 3, 1, 2, 3], 2))  # False
