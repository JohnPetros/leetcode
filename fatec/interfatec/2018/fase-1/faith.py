from collections import Counter

TEST = True


def faith(drawn_nums: list[int], dream_nums: list[int]):
    counter = Counter(drawn_nums)

    items = sorted(counter.items(), key=lambda item: (-item[1], item[0]))

    final_nums = []
    for num in dream_nums:
        final_nums.append(str(items[num - 1][0]))

    print(" ".join(final_nums))


if TEST:
    drawn_nums = [
        2,
        4,
        6,
        8,
        10,
        12,
        1,
        4,
        7,
        9,
        20,
        30,
        22,
        33,
        41,
        2,
        3,
        7,
        32,
        35,
        44,
        60,
        21,
        12,
        1,
        2,
        3,
        4,
        5,
        6,
    ]
    dream_nums = [2, 5, 7, 1, 9, 10]
    faith(drawn_nums, dream_nums)
else:
    n = int(input())
    drawn_nums = []
    for _ in range(n):
        nums = list(map(int, input().split()[:6]))
        drawn_nums += nums
    dream_nums = list(map(int, input().split()[:6]))
    faith(drawn_nums, dream_nums)
