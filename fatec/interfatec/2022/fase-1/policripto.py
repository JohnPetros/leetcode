from string import ascii_lowercase

code = "vdwgzgzwzcahlafwmfuv"
digits = "-3+159013-2+1-390+99989"


signal = "+"

code_index = 0

message = ""

for digit in digits:
    if digit == "+" or digit == "-":
        signal = digit
    else:
        char = code[code_index]
        if code[code_index] == "w":
            message += " "
            code_index += 1

        char = code[code_index]
        char_index = ascii_lowercase.index(char)
        if signal == "-":
            char_index -= int(digit)
        else:
            char_index += int(digit)

        if char_index < 0:
            char_index = char_index + 25 + 1
        elif char_index > 25:
            char_index = char_index - 25 - 1

        message += ascii_lowercase[char_index]

        code_index += 1

print(message)
