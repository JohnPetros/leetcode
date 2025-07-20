from collections import Counter

ages_count = 6
ages = [
    11,
    11,
    9,
    9,
    4,
    4,
]


def calculate_mean(numbers):
    return round(sum(numbers) / len(numbers), 2)


counter = sorted(Counter(ages).items(), key=lambda count: count[1], reverse=True)
mode = []
repeated_count = []
for count in counter:
    if not mode or count[1] in repeated_count:
        mode.append(count[0])
        repeated_count.append(count[1])
mode.sort()
print(f"MODA: {','.join(map(str, mode))}")


print(f"MEDIA: {calculate_mean(ages)}")

ages.sort()
median = ages[ages_count // 2]
if ages_count % 2 == 0:
    median = calculate_mean([ages[ages_count // 2], ages[ages_count // 2 - 1]])
print(f"MEDIANA: {median}")
