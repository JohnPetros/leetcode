def convert_zipcode_to_number(zipcode: str) -> int:
    part1, part2 = zipcode.split("-")
    return int(part1 + part2)


stores_ranges_input = [
    "07503-000 07550-900",
    "07840-500 07850-000",
    "08200-020 08240-500",
]
custumers_ranges_input = [
    "07520-010",
    "07395-550",
    "08236-200",
    "07835-060",
    "07921-370",
    "12410-030",
    "07526-490",
    "08209-000",
    "08541-210",
    "07550-900",
]

stores_ranges = []
customers_ranges = []

for store_range in stores_ranges_input:
    start_zipcode, end_zipcode = store_range.split()
    stores_ranges.append(
        (
            convert_zipcode_to_number(start_zipcode),
            convert_zipcode_to_number(end_zipcode),
        )
    )

stores_ranges.sort()

included_challenge_ranges = []
not_included_challenge_ranges = []

for customer_range in custumers_ranges_input:
    customers_ranges.append((customer_range, convert_zipcode_to_number(customer_range)))

for customer_range in customers_ranges:
    is_included = False
    for store_range in stores_ranges:
        if customer_range[1] >= store_range[0] and customer_range[1] <= store_range[1]:
            is_included = True
            break

    if is_included:
        included_challenge_ranges.append(customer_range)
    else:
        not_included_challenge_ranges.append(customer_range)

for custumer_range in sorted(included_challenge_ranges):
    print(f"{custumer_range[0]} is served by our delivery system")

for custumer_range in sorted(not_included_challenge_ranges):
    print(f"{custumer_range[0]} is not served by our delivery system")
