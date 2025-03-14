def contains_duplicate(numbers: list[int]) -> list[int]:
    memory = set()

    for number in numbers:
        if number in memory:
            return True

        memory.add(number)

    return False


print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
