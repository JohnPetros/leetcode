"Problema da Soma de Subconjuntos"

target = 5
pieces = [1, 2, 3]

dp = [False] * (target + 1)
dp[0] = True

for piece in pieces:
    for index in range(target, piece - 1, -1):
        if dp[index - piece]:
            dp[index] = True

print("SIM" if dp[target] else "NAO")
