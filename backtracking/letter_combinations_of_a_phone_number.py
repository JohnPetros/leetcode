def letter_combinations_of_a_phone_number(phone_number: str) -> list[str]:
    if not phone_number:
        return []

    digits_table = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    combinations = []

    def backtrack(combination: str, phone_number: str):
        if not phone_number:
            combinations.append(combination)
            return

        for character in digits_table[phone_number[0]]:
            backtrack(combination + character, phone_number[1:])

    backtrack("", phone_number)

    return combinations


print(letter_combinations_of_a_phone_number("23"))
