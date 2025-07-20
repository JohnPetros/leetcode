def fibonacci_number(n: int) -> int:
    memo = {0: 0, 1: 1}

    if n not in memo:
        memo[n] = fibonacci_number(n - 2) + fibonacci_number(n - 1)

    return memo[n]


print(fibonacci_number(6))
