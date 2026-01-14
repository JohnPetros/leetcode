def isomorphic_strings(s: str, t: str) -> bool:
    map1 = dict()
    map2 = dict()
    n = len(s)

    for index in range(n):
        char1 = s[index]
        char2 = t[index]

        if char1 in map1 and map1[char1] != char2:
            return False

        if char2 in map2 and map2[char2] != char1:
            return False

        map1[char1] = char2
        map2[char2] = char1

    return True


print(isomorphic_strings("egeg", "adad"))
