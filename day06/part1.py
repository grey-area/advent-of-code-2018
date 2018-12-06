import utils
import numpy as np


# Compute the point that has the largest non-infinite number
# of nearest neighbours

# Kind of hacky
# Return 50 if the minimum element isn't unique, else argmin
def argmin(grid, num_p):
    a1 = np.argmin(grid, axis=2)
    a2 = num_p - 1 - np.argmin(grid[:, :, ::-1], axis=2)
    same = (a1 == a2)
    return np.where(a1==a2, a1, num_p)

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

grid_closest = argmin(grid, len(points))

# We can discount points that are nearest to the edge cells
include = set(range(len(points)))
discount = set(grid_closest[0, :])
discount = discount.union(set(grid_closest[-1, :]))
discount = discount.union(set(grid_closest[:, 0]))
discount = discount.union(set(grid_closest[:, -1]))
include = include - discount
include = np.array(sorted(list(include)))

indices, counts = np.unique(grid_closest[grid_closest < len(points)], return_counts=True)

print(np.max(counts[include]))
