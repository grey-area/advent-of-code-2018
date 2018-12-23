import numpy as np
import re

with open('input') as f:
    data = f.read().splitlines()

mins = np.zeros(3, dtype=np.int64)
maxes = np.zeros(3, dtype=np.int64)

points = np.zeros((1000, 3), dtype=np.int64)
radii = np.zeros(1000, dtype=np.int64)

re_str = '<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)'
for line_i, line in enumerate(data):
    x, y, z, r = [int(i) for i in re.search(re_str, line).groups()]
    point = np.array([x, y, z])
    maxes = np.maximum(maxes, point)
    mins = np.minimum(mins, point)
    points[line_i, :] = point
    radii[line_i] = r

min_val = np.min(mins)
max_val = np.max(maxes)


def compute_counts(points, points2, radii):
    dists = np.sum(np.abs(np.expand_dims(points, 0) - np.expand_dims(points2, 1)), axis=2)
    counts = np.sum(dists <= np.expand_dims(radii, 0), axis=1)

    return counts

best_point = np.mean(points, axis=0).astype(np.int64)
best_count = 0

t = 0
mutation_rate = (max_val - min_val) // 2

mutation = np.random.randint(-mutation_rate, mutation_rate+1, size=(100000, 3))
points2 = np.expand_dims(best_point, 0) + mutation

while True:
    if i % 500 == 0:
        print(i, best_count, mutation_rate, ','.join([str(i) for i in best_point]))
    counts = compute_counts(points, points2, radii)

    highest_count = np.max(counts)
    indices = np.arange(counts.size)
    count_indices = indices[counts == highest_count]
    matching_points = points2[count_indices, :]
    mans = np.sum(np.abs(matching_points))
    best_i = count_indices[np.argmin(mans)]

    p = points2[best_i, :]
    c = counts[best_i]
    if c > best_count or c == best_count and np.sum(np.abs(p)) < np.sum(np.abs(best_point)):
        best_count = c
        best_point = np.copy(p)
        t = 0
    else:
        t += 1

    if t > 20000 and mutation_rate > 100:
        mutation_rate //= 2
        t = 0

    if t > 100000:
        break

    mutation = np.random.randint(-mutation_rate, mutation_rate+1, size=(100, 3))
    points2 = np.expand_dims(best_point, 0) + mutation

print(','.join([str(i) for i in best_point]))
print(np.sum(np.abs(best_point)))
