def quicksort(list: list[int], start_index: int, end_index: int) -> list[int]:
    left_index = start_index
    right_index = end_index
    pivot = list[start_index]

    while left_index <= right_index:

        while list[left_index] < pivot:
            left_index += 1

        while list[right_index] > pivot:
            right_index -= 1

        if left_index <= right_index:
            list[left_index], list[right_index] = list[right_index], list[left_index]
            left_index += 1
            right_index -= 1

    if right_index > start_index:
        quicksort(list, start_index, right_index)

    if left_index < end_index:
        quicksort(list, left_index, end_index)

    return list


numbers = [15, 2, 100, 4, 3, 12]
print(quicksort(numbers, 0, len(numbers) - 1))
