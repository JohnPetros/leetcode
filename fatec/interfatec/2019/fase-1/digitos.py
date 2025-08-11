from math import sqrt


def sieve_of_eratosthenes(limit):
    """
    Gera uma lista de primos até `limit` de forma muito rápida.
    """
    prime_list = [True] * (limit + 1)
    prime_list[0] = prime_list[1] = False

    for number in range(2, int(sqrt(limit)) + 1):
        if prime_list[number]:
            for multiple in range(number * number, limit + 1, number):
                prime_list[multiple] = False

    return prime_list


intervals = [
    "1 100000",
    "3 99999",
]

prime_numbers = sieve_of_eratosthenes(100_000)


for index in range(len(intervals)):
    interval = intervals[index]
    start, end = interval.split()
    count = {number: 0 for number in range(10)}

    for number in range(int(start), int(end) + 1):
        if prime_numbers[number]:
            for digit in str(number):
                count[int(digit)] += 1

    print(f"INTERVALO {index + 1}")
    for number, frequency in count.items():
        print(f"{number}: {frequency}")
