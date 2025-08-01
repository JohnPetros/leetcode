bottles_count = 4567
step = 123


def josephus(n, k):
    if n == 0:
        return None

    survivor = 0

    for i in range(2, n + 1):
        survivor = (survivor + k) % i

    return survivor + 1


print(josephus(bottles_count, step))
