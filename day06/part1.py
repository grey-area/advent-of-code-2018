import utils
import numpy as np


# Compute the point that has the largest non-infinite number
# of nearest neighbours

# TODO:
# - replace hacky argmin
# - tidy up set unions

# Kind of hacky
# Return 50 if the minimum element isn't unique, else argmin
def argmin(grid, num_p):
    a1 = np.argmin(grid, axis=2)
    a2 = num_p - 1 - np.argmin(grid[:, :, ::-1], axis=2)
    same = (a1 == a2)
    return np.where(a1==a2, a1, num_p)

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

closest = argmin(dists, len(points))

# We can discount points that are nearest to the edge cells
include = set(range(len(points)))
discount = set(closest[0, :])
discount = discount.union(set(closest[-1, :]))
discount = discount.union(set(closest[:, 0]))
discount = discount.union(set(closest[:, -1]))
include = include - discount
include = np.array(sorted(list(include)))

indices, counts = np.unique(closest[closest < len(points)], return_counts=True)

print(np.max(counts[include]))
