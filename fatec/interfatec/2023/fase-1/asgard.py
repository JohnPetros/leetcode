# companies_count, defeault_quantity = list(map(int, input().strip().split()))
# days_count = int(input().strip())

# companies = [[0] * 3 for _ in range(companies_count + 1)]

# for _ in range(days_count):
#     day = input()
#     for _ in range(companies_count * 2):
#         origin_company, destiny_company, gas_cylinders_count = list(
#             map(int, input().strip().split())
#         )
#         companies[origin_company - 1][destiny_company - 1] = gas_cylinders_count


companies_count = 3
defeault_quantity = 20
days_count = 4

companies = [[0] * 3 for _ in range(companies_count)]

days_input = [
    [[1, 2, 15], [1, 3, 8], [2, 1, 6], [2, 3, 11], [3, 1, 3], [3, 2, 9]],
    [[1, 2, 4], [1, 3, 7], [2, 1, 8], [2, 3, 12], [3, 1, 8], [3, 2, 5]],
    [[1, 2, 9], [1, 3, 0], [2, 1, 8], [2, 3, 11], [3, 1, 2], [3, 2, 17]],
    [[1, 2, 8], [1, 3, 7], [2, 1, 2], [2, 3, 7], [3, 1, 5], [3, 2, 11]],
]

for index, day_input in enumerate(days_input[0:1]):
    day = index + 1
    for input in day_input:
        origin_company, destiny_company, gas_cylinders_count = input
        companies[origin_company - 1][destiny_company - 1] = gas_cylinders_count

    print(companies)
