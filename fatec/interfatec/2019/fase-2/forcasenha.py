from string import punctuation, ascii_lowercase, ascii_uppercase


def has_digit(string: str):
    for char in string:
        if char.isdigit():
            return True

    return False


def has_letter(string: str):
    for char in string:
        if char.isalpha():
            return True

    return False


def has_punctuation(string: str):
    for char in string:
        if char in punctuation:
            return True

    return False


def has_accent(string: str):
    for char in string:
        if char in "áéíóúâêôãàçÁÉíóÚÃÔÔÕÀÇ":
            return True

    return False


def has_space(string: str):
    for char in string:
        if " " in char:
            return True

    return False


def has_sequence(string: str):
    for index in range(len(string)):
        if (
            index + 1 < len(string)
            and string[index].isdigit()
            and string[index + 1].isdigit()
            and int(string[index]) + 1 == int(string[index + 1])
        ):
            return True

        if (
            index + 1 < len(string)
            and string[index].isalpha()
            and string[index + 1].isalpha()
            and ord(string[index]) + 1 == ord(string[index + 1])
        ):
            return True

    return False


def has_uppercase(string: str):
    for char in string:
        if char in ascii_uppercase:
            return True

    return False


def has_lowercase(string: str):
    for char in string:
        if char in ascii_lowercase:
            return True

    return False


string = "aceF13592"

if (
    not has_accent(string)
    and not has_punctuation(string)
    and not has_space(string)
    and not has_sequence(string)
    and has_digit(string)
    and has_lowercase(string)
    and has_uppercase(string)
    and len(string) >= 6
    and len(string) <= 15
):
    print("True.")
else:
    print("False.")
print()
