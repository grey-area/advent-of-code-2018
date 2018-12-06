import utils
import numpy as np


# Compute the size of the region whose total distance to all points is less than 10000
D = 10000

points = utils.load_data()
max_x = max(points, key=lambda p: p.x).x
max_y = max(points, key=lambda p: p.y).y

x_coords = np.arange(max_x + 1, dtype=np.int32)
y_coords = np.arange(max_y + 1, dtype=np.int32)
dists = np.zeros((max_x + 1, max_y + 1, len(points)), dtype=np.int32)

for p_i, p in enumerate(points):
    x_dists = np.abs(x_coords - p.x)
    y_dists = np.abs(y_coords - p.y)
    p_dists = np.expand_dims(x_dists, 1) + np.expand_dims(y_dists, 0)
    dists[:, :, p_i] = p_dists

total_dists = np.sum(dists, axis=2)
print(np.sum(total_dists < D))
