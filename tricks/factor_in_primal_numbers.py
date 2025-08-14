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


print(factor_in_prime_numbers(630))
