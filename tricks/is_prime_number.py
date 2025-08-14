from math import sqrt


def is_prime_number(number):
    if number == 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for n in range(3, int(sqrt(number)) + 1, 2):
        if number % n == 0:
            return False

    return True
