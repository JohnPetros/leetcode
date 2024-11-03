def permutations(numbers: list[int]) -> list[int]:
    if not numbers or len(numbers) == 1:
        return numbers

    permutations = []
    permutation = []

    def backtrack():
        if len(permutation) == len(numbers):
            permutations.append(permutation.copy())
            return

        for number in numbers:
            if number not in permutation:
                permutation.append(number)
                backtrack()
                permutation.pop()

    backtrack()

    return permutations


print(permutations([1, 2, 3]))
