def palindrome_number(n: int):
    number = n
    if number < 0:
        return False

    reversed_number = 0

    while number:
        digit = number % 10
        number //= 10

        reversed_number = reversed_number * 10 + digit

    return n == reversed_number


print(palindrome_number(121))
print(palindrome_number(-121))
print(palindrome_number(10))
