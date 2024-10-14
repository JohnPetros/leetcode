def combination_sum(candidates: list[int], target: int) -> int:
    valid_combinations = []
    candidates.sort()

    def backtrack(start_index: int, target: int, combination: list[int]):
        if target == 0:
            valid_combinations.append(combination.copy())
            return

        for index in range(start_index, len(candidates)):
            candidate = candidates[index]

            if candidate > target:
                continue

            combination.append(candidate)
            backtrack(index, target - candidate, combination)
            combination.pop()

    backtrack(0, target, [])
    return valid_combinations


print(combination_sum([2, 4, 5], 10))
