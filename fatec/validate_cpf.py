def validate_cpf(cpf: str):
    digits = list(map(int, list(cpf)))
    digits.reverse()
    checker_digits = digits[0:2]
    checker_digits.reverse()
    digits = digits[2:]
    sum = 0

    for index in range(len(digits)):
        sum += digits[index] * (index + 2)

    ten = 0

    if sum % 11 not in [0, 1]:
        ten = 11 - sum % 11
    sum = 0

    digits.insert(0, ten)

    for index in range(len(digits)):
        sum += digits[index] * (index + 2)

    unit = 0
    if sum % 11 not in [0, 1]:
        unit = 11 - sum % 11

    return (
        "VALIDO" if "".join(map(str, checker_digits)) == f"{ten}{unit}" else "IVALIDO"
    )


# cpfs = ["12345678901", "22110779861", "41094483877"]
# cpfs = ["22107779011"]
# cpfs = ["33429738890", "48884567888"]
# cpfs = ["48884567888"]

cpfs_count = int(input())
cpfs = list()

while cpfs_count > 0:
    cpfs.append(input())
    cpfs_count -= 1

for cpf in cpfs:
    print(validate_cpf(str(cpf)))
