def remove_duplicates_from_sorted_array(numbers: list[int]):
    if not numbers:
        return 0

    index = k = 1

    while index < len(numbers):
        if numbers[index] != numbers[k - 1]:
            if index != k:
                numbers[k] = numbers[index]
            k += 1

        index += 1

    return k


print(remove_duplicates_from_sorted_array([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
