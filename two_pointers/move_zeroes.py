def move_zeroes(numbers: list[int]) -> list[int]:
    if all(number == 0 for number in numbers):
        return numbers

    numbers.sort()

    pointer = 0
    while numbers[pointer] == 0:
        numbers.insert(len(numbers), numbers[pointer])
        del numbers[pointer]

    return numbers


# print(move_zeroes([0]))
print(move_zeroes([0, 1, 0, 3, 12]))
