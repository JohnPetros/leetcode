def integer_to_roman(num: int) -> str:
    number = num
    roman_number = ""

    integer_to_roman_table = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    for integer, roman in integer_to_roman_table.items():
        while number >= integer:
            number -= integer
            roman_number += roman

    return roman_number


print(integer_to_roman(1994))
