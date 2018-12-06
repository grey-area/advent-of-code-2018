import utils
import numpy as np


# Compute the size of the region whose total distance to all points is less than 10000
D = 10000

points = utils.load_data()
ys, xs = zip(*points)

x_grid = np.arange(max(xs) + 1, dtype=np.int32)
y_grid = np.arange(max(ys) + 1, dtype=np.int32)
grid = np.zeros((max(xs) + 1, max(ys) + 1, len(points)), dtype=np.int32)

for p_i, p in enumerate(points):
    x_dists = np.abs(x_grid - p.x)
    y_dists = np.abs(y_grid - p.y)
    p_dists = np.expand_dims(x_dists, 1) + np.expand_dims(y_dists, 0)
    grid[:, :, p_i] = p_dists

total_distances = np.sum(grid, axis=2)
print(np.sum(total_distances < D))
