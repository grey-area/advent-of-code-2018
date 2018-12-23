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

m1 = np.min(mins)
m2 = np.max(maxes)

def compute_counts(points, points2, radii):
    dists = np.sum(np.abs(np.expand_dims(points, 0) - np.expand_dims(points2, 1)), axis=2)
    counts = np.sum(dists <= np.expand_dims(radii, 0), axis=1)

    return counts


best_ever = np.mean(points, axis=0).astype(np.int64)
best_ever_count = 0

t = 0
ran = (m2 - m1) // 2

mutation = np.random.randint(-ran, ran+1, size=(50000, 3))
points2 = np.expand_dims(best_ever, 0) + mutation

for i in range(200000):
    if i % 500 == 0:
        print(i, best_ever_count, ran, ','.join([str(i) for i in best_ever]))
    counts = compute_counts(points, points2, radii)

    highest_count = np.max(counts)
    indices = np.arange(counts.size)
    count_indices = indices[counts == highest_count]
    matching_points = points2[count_indices, :]
    mans = np.sum(np.abs(matching_points))
    best_i = count_indices[np.argmin(mans)]

    #best_i = np.argmax(counts)

    p = points2[best_i, :]
    c = counts[best_i]
    if c > best_ever_count or c == best_ever_count and np.sum(np.abs(p)) < np.sum(np.abs(best_ever)):
        best_ever_count = c
        best_ever = np.copy(p)
        t = 0
    else:
        t += 1

    if t > 50:
        ran //= 2
        t = 0

    mutation = np.random.randint(-ran, ran+1, size=(50, 3))
    points2 = np.expand_dims(best_ever, 0) + mutation

print(','.join([str(i) for i in best_ever]))
print(np.sum(np.abs(best_ever)))
