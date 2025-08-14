def josephus(n, k):
    if n == 0:
        return None

    survivor = 0

    for i in range(2, n + 1):
        survivor = (survivor + k) % i

    return survivor + 1


n = 10
k = 2
rest = josephus(n, k)
print(f"Com n={n} e k={k}, o sobrevivente é: {rest}")
