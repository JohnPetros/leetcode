money = 16
coins = {1, 5, 12, 15}

dp = [float("inf")] * (money + 1)

dp[0] = 0

for coin in sorted(coins):
    for index in range(coin, money + 1):
        dp[index] = min(dp[index], dp[index - coin] + 1)

print(dp[money])
