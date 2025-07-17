# profiles_count = int(input())
# required_profiles_counts = []
# required_profiles_counts.append(list(map(int, input().split()[:profiles_count])))
# regions_count = int(input())
# regions = {}
# for _ in range(regions_count):
#   region = input().split()
#   regions[region[0]] = list(map(int, region[1:profiles_count]))


profiles_count = 4
required_profiles_counts = [2, 1, 3, 1]
regions = {
    "ABC01": [5, 3, 8, 1],
    "DRG32": [7, 9, 8, 4],
    "O2932": [3, 3, 2, 9],
}


groups_count_by_region = {}

for region_code, region_profiles_count in regions.items():
    groups_counts = []
    for index in range(profiles_count):
        groups_counts.append(
            region_profiles_count[index] // required_profiles_counts[index]
        )
    groups_count_by_region[region_code] = min(groups_counts)

for region_code, groups_counts in groups_count_by_region.items():
    print(f"{region_code} {groups_counts}")
