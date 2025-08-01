plates = [
    "ABC1D23",
    "QNT8B49",
    "JBO5T18",
    "GDK2W13",
    "GXA4D66",
    "RRP4T27",
    "ACP9A44",
    "SLS7B62",
    "GRO2F24",
    "EQY8F35",
    "QGI1Y43",
    "XKN8V47",
    "IJT5M37",
    "TYE7K36",
    "DZH8I89",
    "QIQ3G43",
    "CDO5S18",
    "MUZ2Y29",
    "YEQ4E35",
    "RLG7H29",
]

parking_spaces = [index + 1 for index in range(15 + 1)]

occupied_parking_spaces = []

for plate in plates:
    space_number = (
        sum([ord(character) for character in plate[:3]])
        + int(plate[3])
        + ord(plate[4])
        + int(plate[5])
        + int(plate[6])
    ) % 15 + 1

    if parking_spaces[space_number - 1]:
        parking_spaces[space_number - 1] = None
        occupied_parking_spaces.append((space_number, plate))

for space in sorted(occupied_parking_spaces, key=lambda space: space[0]):
    print(f"{space[0]} {space[1]}")
