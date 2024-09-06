def string_to_integer(s: str) -> int:
    integer = 0
    string = s.strip()

    if not string:
        return integer

    sign = 1

    first_char = string[0]
    if first_char in ["-", "+"]:
        if first_char == "-":
            sign = -1
        string = string[1:]

    for char in string:
        if not char.isdigit():
            break
        integer = integer * 10 + int(char)

    if integer < -(2**31):
        return -(2**31)

    if integer > 2**31 - 1:
        return 2**31 - 1

    return integer * sign


print(string_to_integer("42"))
# print(string_to_integer("1337c0d3"))
# print(string_to_integer("0-1"))
# print(string_to_integer("   -042"))
# print(string_to_integer("words and 987"))
