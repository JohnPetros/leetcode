from math import sqrt

TESTE = True


def factor_in_prime_numbers(number):
    factors: list[int] = []

    while number % 2 == 0:
        factors.append(2)
        number //= 2

    for i in range(3, int(sqrt(number)) + 1, 2):
        while number % i == 0:
            factors.append(i)
            number //= i

    if number > 2:
        factors.append(int(number))

    return factors


def fatora(n: int):
    factors = factor_in_prime_numbers(n)
    distinct_factors = []
    for factor in factors:
        if factor not in distinct_factors:
            distinct_factors.append(factor)

    print(
        "".join([f"{factor}({factors.count(factor)})" for factor in distinct_factors])
    )


if TESTE:
    fatora(99)
    fatora(9901)
    fatora(9999)
else:
    fatora(int(input()))
