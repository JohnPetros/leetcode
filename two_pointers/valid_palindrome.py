from string import punctuation


def valid_palindrome(string: str):
    string = (
        string.translate(str.maketrans("", "", punctuation)).lower().replace(" ", "")
    )
    left_pointer = 0
    right_pointer = len(string) - 1

    while left_pointer <= right_pointer:
        if string[left_pointer] != string[right_pointer]:
            return False

        left_pointer += 1
        right_pointer -= 1

    return True


print(valid_palindrome("Was it a car or a cat I saw?"))
print(valid_palindrome("tab a cat"))
