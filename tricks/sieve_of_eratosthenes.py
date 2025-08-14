from math import sqrt


def sieve_of_eratosthenes(limit):
    """
    Gera uma lista de primos até `limit` de forma muito rápida.
    """
    prime_numbers = [True] * (limit + 1)
    prime_numbers[0] = prime_numbers[1] = False

    for number in range(2, int(sqrt(limit)) + 1):
        if prime_numbers[number]:
            for multiple in range(number * number, limit + 1, number):
                prime_numbers[multiple] = False

    return prime_numbers


print(sieve_of_eratosthenes(10))
