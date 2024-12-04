def technology_mayor(budget: int, improvements: list[set]):
    improvements.sort(key=lambda improvement: improvement[1], reverse=True)
    total_votes_count = 0

    for improvement in improvements:
        improvement_cost = improvement[0]
        votes_count = improvement[1]

        if improvement_cost <= budget:
            budget -= improvement_cost
            total_votes_count += votes_count

    if total_votes_count == 0:
        return "NO FUNDS"

    return f"{total_votes_count} {budget}"


budget, improvements_count = input().split(" ")
improvements = []

for _ in range(int(improvements_count)):
    improvement_cost, votes_count = input().split(" ")
    improvements.append((int(improvement_cost), int(votes_count)))

print(technology_mayor(int(budget), improvements))


# print(technology_mayor(50, [(20, 50), (10, 500), (35, 750)]))
# print(technology_mayor(100, [(20, 250), (35, 4), (66, 50), (5, 156), (12, 500)]))
# print(technology_mayor(10, [(100, 5), (55, 35)]))
