def reverse_string(string: list[str]) -> list[str]:
    left = 0
    right = len(string) - 1

    while left < right:
        print(left)
        left_element = string[left]
        right_element = string[right]

        string[left] = right_element
        string[right] = left_element

        left += 1
        right -= 1

    return string
    # Time: O(N)
    # Space: O(1)


# print(reverse_string(["h", "e", "l", "l", "o"]))
print(reverse_string(["H", "a", "n", "n", "a", "h"]))
