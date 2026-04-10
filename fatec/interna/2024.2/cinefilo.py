TESTE = True


def knapsack(values, weights, capacity):
    dp = [0] * (capacity + 1)

    for i in range(len(values)):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]


def cinefilo(total_time: int, movies: list[tuple[int, int]]):
    total_time_in_min = total_time * 60

    result = knapsack(
        values=[movie[0] for movie in movies],
        weights=[movie[1] for movie in movies],
        capacity=total_time_in_min,
    )
    print(result)


if TESTE:
    cinefilo(2, [(10, 120), (6, 60), (5, 60)])
else:
    total_time, total_movies = list(map(int, input().split()))
    movies = []
    for i in range(1, total_movies * 2 + 1):
        if i % 2 == 0:
            score, duration = list(map(int, input().split()))
            movies.append((score, duration))
        else:
            input()
    cinefilo(total_time, movies)
