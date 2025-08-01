from math import sqrt


def factor_in_prime_numbers(number):
    factors = []

    while number % 2 == 0:
        factors.append(2)
        number /= 2

    for i in range(3, int(sqrt(number)) + 1, 2):
        if number % i == 0:
            factors.append(i)
            number /= i

    if number > 2:
        factors.append(int(number))

    return factors


inputs = [
    "clara ABC123",
    "ana abc123",
    "bia a1b2c3",
    "duda 1a2b3c",
    "andrecavalcante ZZZzzz",
    "zequinha 1234567890",
    "helena x9x9",
]
outputs = []

for input in inputs:
    username, password = input.split()
    part1 = sum([ord(password[index]) * (index + 1) for index in range(len(password))])
    part2 = "".join(str(prime_number) for prime_number in factor_in_prime_numbers(1586))
    hash = str(part1) + part2
    outputs.append({"username": username, "hash": hash})

outputs.sort(key=lambda output: output["username"])

for output in outputs:
    print(f"usuario: {output['username']}")
    print(f"valor hash: {output['hash']}")
    print("------------------------------")
