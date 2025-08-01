def convert_time_to_miliseconds(time: str):
    minutes, seconds, miliseconds = time.split()
    return miliseconds + (seconds * 1000) + (minutes * 60 * 1000)


def convert_miliseconds_to_time(miliseconds: int):
    return f"{(miliseconds // 60 * 1000):02}:{(miliseconds % 60 * 1000 // 1000):02}:{(miliseconds // 1000):03}"


players_count = 8

inputs = [
    "8",
    "1 Theo Dubois",
    "2 Lola Mallet",
    "3 Lorium Nbani",
    "4 Keiko Sato",
    "5 Emily Valdorf",
    "6 Yohanes Tetrakis",
    "7 Yousef Rosemberg",
    "8 Liam Chub",
    "8 Cubo 3x3x3",
    "1 0:31:000 0:26:000 0:00:000 0:30:000 0:00:000",
    "2 0:18:000 0:18:000 0:19:000 0:20:000 0:22:000",
    "3 0:09:000 0:10:000 0:11:000 0:12:000 0:13:000",
    "4 0:17:000 0:18:000 0:19:000 0:20:000 0:21:000",
    "5 0:10:000 0:11:000 0:12:000 0:13:000 0:14:000",
    "6 0:00:000 0:00:000 0:00:000 0:00:000 0:00:000",
    "7 0:16:000 0:18:000 0:20:000 0:22:000 0:24:000",
    "8 0:00:000 0:00:000 0:00:000 0:00:000 0:00:000",
    "FIM",
]

players_count = 0

players_count = int(input())
players = [None for _ in range(players_count)]

for _ in range(players_count):
    id, name, lastname = input().strip().split()
    players[int(id) - 1] = {
        "id": id,
        "name": name,
        "lastname": lastname,
    }

cubes = []


while True:
    _input = input().strip()
    if _input == "FIM":
        break

    plays_count, cube_name = _input.split(maxsplit=1)
    cube = {"name": cube_name, "players": []}
    times = []

    for _ in range(int(plays_count)):
        id, time1, time2, time3, time4, time5 = input().strip().split()
        median = 0
        times = [time1, time2, time3, time4, time5]
        dnf_count = times.count("DNF")
        times = [
            float("inf") if time == "DNF" else convert_time_to_miliseconds(time)
            for time in times
        ]
        best = min(times)
        worst = max(times)

        if dnf_count == 5:
            median = "DNF"
            best = "DNF"
        elif dnf_count == 1:
            times = [time for time in times if time not in [best, worst]]
            sum(times) / len(times)
        elif dnf_count >= 2:
            median = "DNF"

        cube["players"].append({"id": id, "median": median, "best": best})

        cube["players"] = sorted(
            cube["players"], key=lambda player: (player["median"], player["best"])
        )
        cubes.append(cube)


print(".Id.Nome.......................Media......Melhor")

for cube in cubes:
    print(cube["name"])
    for player in cube["players"]:
        id = player["id"]
        median = (
            convert_miliseconds_to_time(player["median"])
            if player["median"] != "DNF"
            else "DNF"
        )
        best = (
            convert_miliseconds_to_time(player["median"])
            if player["median"] != "DNF"
            else "DNF"
        )

        print(f"{id} {players[int(id) - 1]['name']} {median} {best}")
