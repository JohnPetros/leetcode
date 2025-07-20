def fibonacci_number(n: int) -> int:
    if n == 0 and n == 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for index in (2, n + 1):
        dp[index] = dp[index - 2] + dp[index - 1]

    return dp[n]


print(fibonacci_number(6))
