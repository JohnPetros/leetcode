def first_missing_positive(numbers: list[int]) -> int:
    total_numbers = len(numbers)

    for index in range(total_numbers):
        number = numbers[index]
        while 1 <= number and numbers[number - 1] != number:
            numbers[number - 1], numbers[index] = number, numbers[number - 1]

    for index in range(total_numbers):
        if numbers[index] != index + 1:
            return index + 1

    return total_numbers + 1
