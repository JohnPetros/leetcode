import math


def euclidean_distance_2d(point1: tuple[int], point2: tuple[int]) -> int:
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


clusters_count, radius = list(map(int, input().strip().split()))
points = []
for _ in range(clusters_count):
    x, y = list(map(int, input().strip().split()))
    points.append((x, y))


# clusters_count = 5
# radius = 2
# points = [(7, 7), (11, 7), (9, 7), (6, 8), (13, 8)]

clusters_count = 7
radius = 38
points = [
    (-966, -351),
    (-10, 899),
    (517, 524),
    (-376, -594),
    (-595, -696),
    (362, -943),
    (978, 945),
]

clusters = []

for point in points:
    if not clusters:
        clusters.append([point, [point]])
        continue

    nearest_cluster = sorted(
        clusters, key=lambda cluster: euclidean_distance_2d(cluster[0], point)
    )[0]

    if euclidean_distance_2d(nearest_cluster[0], point) <= radius:
        nearest_cluster[1].append(point)

        points_count = len(nearest_cluster[1])
        nearest_cluster[0] = (
            int(sum([point[0] for point in nearest_cluster[1]]) / points_count),
            int(sum([point[1] for point in nearest_cluster[1]]) / points_count),
        )

        clusters = [
            cluster if cluster[0] != nearest_cluster[0] else nearest_cluster
            for cluster in clusters
        ]
    else:
        clusters.append([point, [point]])


print(len(clusters))
for cluster in clusters:
    print(f"{cluster[0][0]} {cluster[0][1]}")
