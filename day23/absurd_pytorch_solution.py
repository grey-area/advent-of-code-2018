import numpy as np
import re
import torch
import torch.optim as optim
from torch.nn.functional import relu

with open('input') as f:
    data = f.read().splitlines()

points = np.zeros((len(data), 3), dtype=np.int64)
radii = np.zeros(len(data), dtype=np.int64)

re_str = '<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)'
for line_i, line in enumerate(data):
    x, y, z, r = [int(i) for i in re.search(re_str, line).groups()]
    point = np.array([x, y, z])
    points[line_i, :] = point
    radii[line_i] = r

# Start at the mean of the points
point = torch.tensor(np.mean(points, axis=0), requires_grad=True)

points_tns = torch.tensor(points.astype(np.float64), requires_grad=False)
radii_tns = torch.tensor(radii.astype(np.float64), requires_grad=False)
alpha = 1000000

# Use gradient descent to get close to our answer
for i in range(15000):
    if point.grad is not None:
        point.grad.data.zero_()
    dists = torch.sum(torch.abs(point - points_tns), dim=1)
    score = torch.mean(relu(dists - radii_tns)) + 0.05 * torch.sum(torch.abs(point))
    score.backward()
    point.data -= alpha * point.grad.data
    if i % 3000 == 0:
        alpha /= 10


def compute_counts(points, point, radii):
    return np.sum(np.sum(np.abs(points - np.expand_dims(point, axis=0)), axis=1) <= radii)

# From that initial point, check a 10x10x10 grid
best_count = 0
smallest_dist_from_origin = float('inf')
initial_point = point.detach().numpy().astype(np.int64)

for x_delta in range(-10, 11, 1):
    for y_delta in range(-10, 11, 1):
        for z_delta in range(-10, 11, 1):
            delta = np.array([x_delta, y_delta, z_delta])
            point = initial_point + delta
            count = compute_counts(points, point, radii)

            if count > best_count:
                best_count = count
                smallest_dist_from_origin = np.sum(np.abs(point))
            elif count == best_count:
                smallest_dist_from_origin = min(smallest_dist_from_origin, np.sum(np.abs(point)))

print(smallest_dist_from_origin)
