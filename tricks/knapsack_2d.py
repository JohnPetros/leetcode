# Dois tipos de restrição simultâneas (ex: peso e volume).
def knapsack_2d(values, weights1, weights2, cap1, cap2):
    dp = [[0] * (cap2 + 1) for _ in range(cap1 + 1)]
    for i in range(len(values)):
        for w1 in range(cap1, weights1[i] - 1, -1):
            for w2 in range(cap2, weights2[i] - 1, -1):
                dp[w1][w2] = max(
                    dp[w1][w2], dp[w1 - weights1[i]][w2 - weights2[i]] + values[i]
                )
    return dp[cap1][cap2]


# Teste — peso e volume
values = [10, 15, 22]
weights1 = [3, 4, 5]  # peso
weights2 = [2, 3, 4]  # volume
print(knapsack_2d(values, weights1, weights2, 8, 6))  # 25
