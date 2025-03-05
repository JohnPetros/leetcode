from math import gcd


def greatest_common_divisor_of_string(string1: str, string2: str):
    if string1 + string2 != string2 + string1:
        return ""

    return string1[: gcd(len(string1), len(string2))]


print(greatest_common_divisor_of_string("ABCABC", "ABC"))
print(greatest_common_divisor_of_string("ABABABABAB", "ABAB"))
print(greatest_common_divisor_of_string("LEET", "CODE"))
