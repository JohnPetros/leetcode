def longest_palindrome_substring(string: str) -> list[str]:
    if len(string) == 1:
        return string

    def is_palindrome(left_pointer: int, right_pointer: int):
        nonlocal max_left_pointer, max_right_pointer

        while (
            left_pointer >= 0
            and right_pointer < len(string)
            and string[left_pointer] == string[right_pointer]
        ):
            if (
                right_pointer - left_pointer + 1
                > max_right_pointer - max_left_pointer + 1
            ):

                max_right_pointer, max_left_pointer = right_pointer, left_pointer

            left_pointer -= 1
            right_pointer += 1

    max_left_pointer = max_right_pointer = 0
    for index in range(len(string)):
        start_index = end_index = index

        while (
            start_index >= 0
            and end_index < len(string) - 1
            and string[start_index] == string[end_index]
        ):
            start_index -= 1
            end_index += 1

    for index in range(len(string)):
        is_palindrome(index, index)
        is_palindrome(index, index + 1)

    return string[max_left_pointer : max_right_pointer + 1]


print(longest_palindrome_substring("babad"))
print(longest_palindrome_substring("cbbd"))
print(longest_palindrome_substring("bb"))
