def longest_palindromic_substring(string: str) -> str:
    longest_palindromic = ""
    longest_palindromic_length = 0

    def get_longest_palindromic(
        index: int,
        isOdd: bool,
        longest_palindromic: str,
        longest_palindromic_length: int,
    ):
        left_pointer, right_pointer = index, index + isOdd if 1 else 0

        while (
            left_pointer >= 0
            and right_pointer < len(string)
            and string[left_pointer] == string[right_pointer]
        ):
            palindromic_length = right_pointer - left_pointer + 1
            if palindromic_length > longest_palindromic_length:
                longest_palindromic_length = palindromic_length
                longest_palindromic = string[left_pointer : right_pointer + 1]

            left_pointer -= 1
            right_pointer += 1

        return longest_palindromic, longest_palindromic_length

    for index in range(len(string)):
        longest_palindromic, longest_palindromic_length = get_longest_palindromic(
            index=index,
            isOdd=False,
            longest_palindromic=longest_palindromic,
            longest_palindromic_length=longest_palindromic_length,
        )
        longest_palindromic, longest_palindromic_length = get_longest_palindromic(
            index=index,
            isOdd=True,
            longest_palindromic=longest_palindromic,
            longest_palindromic_length=longest_palindromic_length,
        )

    return longest_palindromic


print(longest_palindromic_substring("babad"))
