def next_permutation(numbers: list[int]) -> list[int]:
    i = len(numbers) - 2

    while i >= 0 and numbers[i] >= numbers[i + 1]:
        i -= 1

    if i >= 0:
        j = len(numbers) - 1
        while j >= 0 and numbers[j] <= numbers[i]:
            j -= 1
        numbers[i], numbers[j] = numbers[j], numbers[i]

    numbers[i + 1 :] = reversed(numbers[i + 1 :])

    return numbers


# print(next_permutation([1, 2, 3]))
# print(next_permutation([3, 2, 1]))
print(next_permutation([2, 3, 1]))
