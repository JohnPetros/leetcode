def unbounded_knapsack(capacity: int, items: list[tuple[int, int]]) -> int:
    dp = [0] * (capacity + 1)

    for weight, value in items:
        for i in range(weight, capacity + 1):
            dp[i] = max(dp[i], dp[i - weight] + value)

    return dp[capacity]


capacity = 100
items = [
    (5, 10),
    (17, 100),
    (9, 1000),
]

result = unbounded_knapsack(capacity, items)
print(result)
