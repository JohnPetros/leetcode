def unbounded_knapsack(capacity: int, items: list[tuple[int, int]]) -> int:
    dp = [0] * (capacity + 1)

    for weight, value in items:
        for i in range(weight, capacity + 1):
            dp[i] = max(dp[i], dp[i - weight] + value)

    return dp[capacity]


capacity = 8
items = [
    (3, 10),  # weight, value
    (4, 15),
    (5, 22),
]

result = unbounded_knapsack(capacity, items)
print(f"Resultado final: {result}")  # Saída esperada: 32
