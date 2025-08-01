inputs = ["65 66 67 49 67 51 52", "88 88 88 48 48 48 48", "23 45 72 23 89 42 43"]


def validate_plate(plate: str) -> str:
    if len(plate) < 7:
        return "ERRO"

    if (
        plate[0].isalpha()
        and plate[1].isalpha()
        and plate[2].isalpha()
        and plate[3].isdecimal()
        and plate[4].isdecimal()
        and plate[5].isdecimal()
        and plate[6].isdecimal()
    ):
        return "ANTIGA"

    if (
        plate[0].isalpha()
        and plate[1].isalpha()
        and plate[2].isalpha()
        and plate[3].isdecimal()
        and plate[4].isalpha()
        and plate[5].isdecimal()
        and plate[6].isdecimal()
    ):
        return "MERCOSUL"

    return "ERRO"


for input in inputs:
    plate = "".join([chr(int(character)) for character in input.split()])
    print(validate_plate(plate))
