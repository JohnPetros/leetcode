def super_cheat(ch: int, message: str):
    TABLE = {
        " ": 0,
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26,
    }

    decrypted_message = ""

    for character in message:
        m = TABLE[character]
        c = (m + ch) % 27

        for decrypted_character, number in TABLE.items():
            if number == c:
                decrypted_message += decrypted_character

    print(decrypted_message)


# ch = int(input())
# message = input()

super_cheat(10, "JHZTEBEHQTRCFVRE")
super_cheat(26, "QBMNFJSBTAOBPAUFNANVOEJBM")
super_cheat(7, "FUMYFUMBWUTIUKUTWHFINMUWUH")
