def insertion_sort(numbers: list[int]) -> list[int]:
    n = len(numbers)

    for index in range(1, n):
        number = numbers[index]
        previous_index = index - 1

        while previous_index >= 0 and numbers[previous_index] > number:
            numbers[previous_index + 1] = numbers[previous_index]
            previous_index -= 1

        numbers[previous_index + 1] = number

    return numbers


print(insertion_sort([4, 7, 2, 5, 4, 0]))
