# players_count = int(input())
# players = []

# for _ in range(players_count):
#     player_name = input()
#     players.append({"name": player_name, "plays": [], "guesses": []})

# rounds_count = int(input())
# order = "plays"
# for _ in range(rounds_count * 2):
#     if order == "plays":
#         plays = list(map(int, input().split()[:players_count]))
#         for index in range(players_count):
#             players[index]["plays"].append(plays[index])
#         order = "guesses"
#     else:
#         guesses = list(map(int, input().split()[:players_count]))
#         for index in range(players_count):
#             players[index]["guesses"].append(guesses[index])
#         order = "plays"

rounds_count = 3
players = [
    {
        "name": "LILO",
        "plays": [2, 1, 2],
        "guesses": [3, 4, 3],
        "score": 0,
    },
    {
        "name": "STITCH",
        "plays": [0, 0, 1],
        "guesses": [2, 1, 1],
        "score": 0,
    },
]

for player in players:
    for index in range(rounds_count):
        if player["plays"][index] == player["guesses"][index]:
            player["score"] += 1


sorted_players = sorted(players, key=lambda player: player["score"], reverse=True)

if sorted_players[0]["score"] == sorted_players[1]["score"]:
    print("EMPATE")
else:
    print(f"{sorted_players[0]['name']} GANHOU")
