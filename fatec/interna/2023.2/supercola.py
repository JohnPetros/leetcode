import string

TESTE = True


def supercola(ch: int, cypher: str):
    letters = list(string.ascii_uppercase)  # A até Z
    numbers = list(range(1, 27))  # 1 até 26

    table = {" ": 0}
    for letter, number in zip(letters, numbers):
        table[letter] = number

    inversed_table = {0: " "}
    for letter, number in zip(letters, numbers):
        inversed_table[number] = letter

    message = []

    for char in cypher:
        original = (table[char] + ch) % 27
        message.append(inversed_table[original])

    print("".join(message))


if TESTE:
    supercola(10, "JHZTEBEHQTRCFVRE")
    supercola(26, "QBMNFJSBTAOBPAUFNANVOEJBM")
    supercola(7, "FUMYFUMBWUTIUKUTWHFINMUWUH")
    supercola(1, "BCDE")
else:
    ch = int(input())
    cypher = input()
    supercola(ch, cypher)
