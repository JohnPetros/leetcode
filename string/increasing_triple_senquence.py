def increasing_triplet_sequence(numbers: list[int]) -> bool:
    if len(numbers) < 3:
        return False

    number_1 = number_2 = number_3 = float("inf")

    for number in numbers:
        if number < number_1:
            number_1 = number
        elif number_1 < number < number_2:
            number_2 = number
        elif number_1 < number_2 < number < number_3:
            return True

    return False


print(increasing_triplet_sequence([1, 2, 3, 4, 5]))
print(increasing_triplet_sequence([5, 4, 3, 2, 1]))
print(increasing_triplet_sequence([2, 1, 5, 0, 4, 6]))
print(increasing_triplet_sequence([2, 4, -2, -3]))
print(increasing_triplet_sequence([[1, 2, 2, 1]]))
