TESTE = True


def fibonacci(n: int) -> int:
    fib = [0] * (n + 1)
    fib[1] = 1
    if n >= 2:
        fib[2] = 1
    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[-1]


def zookeeper(capacity: int, proposals: list[tuple[int, float]]):
    total = 0
    for prop in proposals:
        fib = fibonacci(prop[0])
        if fib <= capacity:
            total += prop[1]
    print(f"{total:.2f}")


if TESTE:
    zookeeper(10, [(3, 100.0), (5, 200.0), (7, 500.0)])
    zookeeper(30, [(8, 150.0), (4, 200.0), (5, 50.0), (2, 300.0)])
else:
    s, p = list(map(int, input().split()))
    proposals = []
    for _ in range(p):
        n, v = input().split()
        proposals.append((int(n), float(v)))
    zookeeper(s, proposals)
