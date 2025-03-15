def roman_to_integer(roman_number: str) -> int:
    roman_integer_mapper = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    integer = 0

    for index in range(len(roman_number)):
        if (
            index < len(roman_number) - 1
            and roman_integer_mapper[roman_number[index]]
            < roman_integer_mapper[roman_number[index + 1]]
        ):
            integer -= roman_integer_mapper[roman_number[index]]
        else:
            integer += roman_integer_mapper[roman_number[index]]

    return integer


print(roman_to_integer("MCMXCIV"))
