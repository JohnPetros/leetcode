def divide_two_integers(dividend: int, divisor: int) -> int:
    if dividend == 0 or divisor == 0:
        return 0

    MAX_INTEGER = 2**31 - 1
    MIN_INTEGER = -(2**31)

    is_quotient_negative = True
    quotient = 0

    if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
        is_quotient_negative = False
        quotient = 0

    dividend = abs(dividend)
    divisor = abs(divisor)
    while dividend >= divisor:
        large_divisor = divisor
        subtractions_times = 1

        while large_divisor * 2 <= dividend:
            large_divisor *= 2
            subtractions_times *= 2

        dividend -= large_divisor
        quotient += subtractions_times

    quotient = -quotient if is_quotient_negative else quotient

    if quotient > MAX_INTEGER:
        return MAX_INTEGER
    if quotient < MIN_INTEGER:
        return MIN_INTEGER
    return quotient


print(divide_two_integers(-7, 3))
