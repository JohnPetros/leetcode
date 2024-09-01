from math import fmod


def reverse_integer(_integer: int):
    MAX = 2147483648 - 1
    MIN = -2147483648
    reverse_integer = 0
    integer = _integer

    while integer:
        digit = fmod(integer, 10)
        integer = int(integer / 10)

        if reverse_integer > MAX // 10 or (
            reverse_integer == MAX // 10 and digit >= MAX % 10
        ):
            return 0
        if reverse_integer < MIN // 10 or (
            reverse_integer == MIN // 10 and digit <= MIN % 10
        ):
            return 0

        reverse_integer = reverse_integer * 10 + digit

    return int(reverse_integer)


print(reverse_integer(123))
print(reverse_integer(-123))
print(reverse_integer(120))
