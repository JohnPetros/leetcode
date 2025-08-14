def is_primorial(number):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]

    # Primorials crescem rapidamente. O último primorial que cabe em 64 bits é o produto dos primeiros 17 primos.
    # O produto dos primeiros 18 primos já excede 2^63 - 1.

    current_product = 1
    prime_index = 0

    while current_product < number and prime_index < len(primes):
        current_product *= primes[prime_index]
        prime_index += 1

    return "S" if current_product == number else "N"


# Exemplo de uso
integer = 9223372036854775807
print(is_primorial(integer))

integer_primorial = 510510
print(is_primorial(integer_primorial))

integer_not_primorial = 630
print(is_primorial(integer_not_primorial))
