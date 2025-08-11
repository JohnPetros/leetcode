from string import ascii_uppercase
from itertools import permutations

string_count = 8
minimum_support = 400
minimum_confidence = 200
strings = [
    "SAOPUL",
    "SORCAB",
    "FATEC",
    "BRASIL",
    "SAOBENT",
    "ATLEICO",
    "ITU",
    "JAU",
]

pairs = list(permutations(ascii_uppercase, 2))
# pairs = [("A", "R"), ("R", "A")]
results = []

for pair in pairs:
    valid_strings = len(
        [string for string in strings if pair[0] in string and pair[1] in string]
    )
    support = int((valid_strings / string_count) * 1000)

    if len([string for string in strings if pair[0] in string]) > 0:
        confidence = int(
            valid_strings
            / len([string for string in strings if pair[0] in string])
            * 1000
        )
    if confidence >= minimum_confidence and support >= minimum_support:
        results.append((pair, (confidence, support)))

print(results)

for result in results:
    print(
        f"{result[0][0]} -> {result[0][1]} [{str(result[1][0] / 1000).ljust(5, '0')} {str(result[1][1] / 1000).ljust(5, '0')}]"
    )
