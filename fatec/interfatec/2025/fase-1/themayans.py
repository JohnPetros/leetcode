system = {
    "*": 0,
    ".": 1,
    "..": 2,
    "...": 3,
    "....": 4,
    "-": 5,
    "-.": 6,
    "-..": 7,
    "-...": 8,
    "-....": 9,
    "--": 10,
    "--.": 11,
    "--..": 12,
    "--...": 13,
    "--....": 14,
    "---": 15,
    "---.": 16,
    "---..": 17,
    "---...": 18,
    "---....": 19,
}

numbers = [
    ". --..",
    "-. -- --....",
    ". * * -...",
    "....",
    ". . . .",
    "---",
    "- - -",
    "-. -. -. -. -. -. -. -.",
    "*",
]

powers = [20**index for index in range(8)]

for number in numbers:
    parts = []
    for index, digit in enumerate(number.split()[::-1]):
        parts.append(system[digit] * powers[index])
    print(sum(parts))
