from collections import Counter


def maximum_length_substring_with_two_occurrences(string: str) -> int:
    left_pointer, right_pointer = 0, 0
    counter = Counter(string[0])
    maximum_length = 1

    while right_pointer < len(string) - 1:
        right_pointer += 1
        last_character = string[right_pointer]
        counter[last_character] += 1

        while counter[last_character] == 3:
            first_character = string[left_pointer]
            counter[first_character] -= 1
            left_pointer += 1

        maximum_length = max(maximum_length, right_pointer - left_pointer + 1)

    return maximum_length
    # Time Complexity: O(n)
    # Space Complexity: O(1)


print(maximum_length_substring_with_two_occurrences("bcbbbcba"))
