def longest_common_prefix(strs: list[str]) -> str:
    chars = []
    min_lengh = min([len(str) for str in strs])

    for index in range(min_lengh):
        if len(set([str[index] for str in strs])) != 1:
            break

        chars.append(strs[0][index])

    return "".join(chars)
    # Tim: O(N)
    # Space: O(N)


print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
