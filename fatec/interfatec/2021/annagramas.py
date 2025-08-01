from collections import Counter

inputs = [
    "FORORFRDOFR",
    "FOR",
    "AABAABAA",
    "AABA",
    "HOJE",
    "NAOEHOJE",
    "ABBA",
    "BAAB",
    "PIRULITOQUEBATEBATEPIRULITOUQUEJABATEU",
    "BATE",
    "ABCDEFGHIJKLMNOPQRSTUVWXY",
    "Z",
]

s1 = ""
s2 = ""

for input_str in inputs:
    if not s1:
        s1 = input_str
        continue

    s2 = input_str

    if len(s2) > len(s1):
        print("ERRO")
    else:
        count = 0
        len_s2 = len(s2)
        len_s1 = len(s1)

        s2_counter = Counter(s2)
        window_counter = Counter(s1[:len_s2])

        if window_counter == s2_counter:
            count += 1

        for index in range(len_s2, len_s1):
            character_to_add = s1[index]
            window_counter[character_to_add] += 1

            character_to_remove = s1[index - len_s2]
            window_counter[character_to_remove] -= 1

            if window_counter[character_to_remove] == 0:
                del window_counter[character_to_remove]

            if window_counter == s2_counter:
                count += 1

        print(count)

    s1 = ""
    s2 = ""
