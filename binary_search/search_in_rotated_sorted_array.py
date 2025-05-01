def search_in_rotated_sorted_array(array: list[int], target: int) -> int:
    left_pointer = 0
    right_pointer = len(array) - 1

    while left_pointer < right_pointer:
        middle_pointer = (left_pointer + right_pointer) // 2

        if array[middle_pointer] > array[right_pointer]:
            left_pointer = middle_pointer + 1
        else:
            right_pointer = middle_pointer
            
    minimum_index = left_pointer

    if minimum_index == 0:
        left_pointer, right_pointer = 0, len(array) - 1
    elif target >= array[0] and target <= array[minimum_index - 1]:
        left_pointer, right_pointer = 0, minimum_index - 1
    else:
        left_pointer, right_pointer = minimum_index, len(array) - 1
        
        
    while left_pointer <= right_pointer:
        middle_pointer = (left_pointer + right_pointer) // 2
        
        if array[middle_pointer] == target:
            return middle_pointer
        
        if array[middle_pointer] < target:
            left_pointer = middle_pointer + 1
        else:
            right_pointer = middle_pointer - 1
    

    return -1
    # Time complexity: O(log n)
    # Space complexity: O(1)


print(search_in_rotated_sorted_array([4,5,6,7,0,1,2], 3))  # 1
