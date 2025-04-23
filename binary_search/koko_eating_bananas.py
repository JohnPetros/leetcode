from math import ceil


def koko_eating_bananas(piles: list[int], hours: int) -> int:
    left_pointer = 1
    right_pointer = max(piles)

    while left_pointer < right_pointer:
        middle_pointer = (left_pointer + right_pointer) // 2
        total_hours = sum(ceil(pile / middle_pointer) for pile in piles)

        if total_hours <= hours:
            right_pointer = middle_pointer
        else:
            left_pointer = middle_pointer + 1

    return left_pointer
    # Time complexity: O(n * log(max(piles)))
    # Space complexity: O(1)


print(koko_eating_bananas([3, 6, 7, 11], 8))
print(koko_eating_bananas([30, 11, 23, 4, 20], 5))
print(koko_eating_bananas([30, 11, 23, 4, 20], 6))
