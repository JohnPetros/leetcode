def bubble_sort(numbers: list[int]) -> list[int]:
    n = len(numbers)
    for j in range(1, n):
        for i in range(n - j):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

    return numbers


print(bubble_sort([4, 9, 2, 1, 7, 8]))
