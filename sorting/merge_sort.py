from typing import Union


def merge_sort(
    numbers: list[int], start: int = 0, end: Union[int, None] = None
) -> list[int]:

    def merge(numbers: list[int], start: int, middle: int, end: int):
        left = numbers[start:middle]
        right = numbers[middle:end]
        left_top, right_top = 0, 0

        for index in range(start, end):
            if left_top >= len(left):
                numbers[index] = right[right_top]
                right_top += 1
            elif right_top >= len(right):
                numbers[index] = left[left_top]
                left_top += 1
            elif left[left_top] < right[right_top]:
                numbers[index] = left[left_top]
                left_top += 1
            else:
                numbers[index] = right[right_top]
                right_top += 1

    if end is None:
        end = len(numbers)

    if end - start > 1:
        middle = (end + start) // 2
        print(start, middle, end)

        merge_sort(numbers, start, middle)
        merge_sort(numbers, middle, end)
        merge(numbers, start, middle, end)


numbers = [4, 7, 2, 6, 4, 1, 8, 3]
merge_sort(numbers)
print(numbers)
