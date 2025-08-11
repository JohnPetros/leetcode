from math import sqrt


def euclidean_distance_2d(point1: tuple[int], point2: tuple[int]) -> int:
    x1, y1 = point1
    x2, y2 = point2
    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return int(distance)


bochas_per_player = 3
round_count = 2

bochas = [
    "24000 2000",
    "24010 2000",
    "24000 2320",
    "23950 2000",
    "24060 2000",
    "23730 2000",
    "24000 1760",
    "22000 2200",
    "22000 1730",
    "22000 2330",
    "21760 2200",
    "21320 2200",
    "22000 2220",
    "22000 1850",
]

bolim = None
total_bochas = 0
bochas_index = 0
player1_score = 0
player2_score = 0

for round_index in range(round_count):
    player1_bochas = []
    player2_bochas = []

    while (
        len(player1_bochas) != bochas_per_player
        or len(player2_bochas) != bochas_per_player
    ):
        if not bolim:
            x, y = bochas[bochas_index].split()
            bolim = (int(x), int(y))
        else:
            x, y = bochas[bochas_index].split()
            if len(player1_bochas) == bochas_per_player:
                player2_bochas.append(euclidean_distance_2d((int(x), int(y)), bolim))
            else:
                player1_bochas.append(euclidean_distance_2d((int(x), int(y)), bolim))

        bochas_index += 1

    player1_bochas.sort()
    player2_bochas.sort()
    player1_bochas_index = 0
    player2_bochas_index = 0

    while player1_bochas and player2_bochas and player1_bochas[0] == player2_bochas[0]:
        player1_bochas.pop(0)
        player2_bochas.pop(0)

    if not player1_bochas or not player2_bochas:
        continue

    if player1_bochas[0] < player2_bochas[0]:
        for bocha in player1_bochas:
            if bocha < player2_bochas[0]:
                player1_score += 1
    else:
        for bocha in player2_bochas:
            if bocha < player1_bochas[0]:
                player2_score += 1

    bolim = None


print(f"PONTOS DAS BOCHAS BRANCAS = {player1_score}")
print(f"PONTOS DAS BOCHAS VERMELHAS = {player2_score}")
print(f"VENCEDOR: BOCHAS {'BRANCAS' if player1_score > player2_score else 'VERMELHAS'}")
