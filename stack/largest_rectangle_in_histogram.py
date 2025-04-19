def largest_rectangle_in_histogram(heights: list[int]) -> int:
    stack = list()
    max_area = 0

    for index in range(len(heights)):
        last_index = index
        while len(stack) and stack[-1][0] > heights[index]:
            rectangle = stack.pop()
            area = rectangle[0] * (index - rectangle[1])
            max_area = max(area, max_area)
            last_index = rectangle[1]
        stack.append((heights[index], last_index))

    last_index = len(heights)
    while len(stack):
        area = stack[-1][0] * (last_index - stack[-1][1])
        max_area = max(area, max_area)
        stack.pop()

    return max_area
    # Time complexity: O(n)
    # Space complexity: O(n)


print(largest_rectangle_in_histogram([2, 1, 5, 6, 2, 3]))
print(largest_rectangle_in_histogram([2, 4]))
