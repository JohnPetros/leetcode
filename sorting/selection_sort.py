def selection_sort(numbers: list[int]) -> list[int]:
    numbers_count = len(numbers)

    for first_number_index in range(numbers_count - 1):
        less_number_index = first_number_index

        for second_number_index in range(first_number_index, numbers_count):
            if numbers[second_number_index] < numbers[less_number_index]:
                less_number_index = second_number_index

        if first_number_index != less_number_index:
            numbers[first_number_index], numbers[less_number_index] = (
                numbers[less_number_index],
                numbers[first_number_index],
            )
    return numbers


print(selection_sort([7, 5, 1, 8, 3]))
