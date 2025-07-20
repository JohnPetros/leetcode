# pairs_count = int(input())
# for _ in range(pairs_count):
#     pattern1, pattern2 = input()
#     left_hash_map[pattern1] = left_hash_map.get(pattern1, 0) + 1
#     right_hash_map[pattern1] = right_hash_map.get(pattern2, 0) + 1

pairs_count = 4

left_hash_map = dict()
right_hash_map = dict()


pairs = [
    "1 2",
    "2 3",
    "3 4",
    "4 5",
    "5 6",
    "6 7",
    "7 8",
    "8 9",
    "9 10",
]

for pair in pairs:
    pattern1, pattern2 = pair.split()
    left_hash_map[pattern1] = left_hash_map.get(pattern1, 0) + 1
    right_hash_map[pattern2] = right_hash_map.get(pattern2, 0) + 1

results = []
results.extend(
    [
        (pattern, frequency, "E")
        for pattern, frequency in left_hash_map.items()
        if frequency > 1
    ]
)
results.extend(
    [
        (pattern, frequency - 1, "D")
        for pattern, frequency in right_hash_map.items()
        if frequency > 1
    ]
)


if not results:
    print("SEM TROCAS DESTA VEZ")
else:
    for result in sorted(results, key=lambda result: (int(result[0]), result[2])):
        print(f"{result[0]} {result[2]} {result[1]}")
