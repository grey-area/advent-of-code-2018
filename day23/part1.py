import numpy as np
import re

with open('input') as f:
    data = f.read().splitlines()

max_r = -float('inf')
max_point = None

re_str = '<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)'
for line_i, line in enumerate(data):
    x, y, z, r = [int(i) for i in re.search(re_str, line).groups()]

    if r > max_r:
        max_r = r
        max_point = np.array([x, y, z])

count = 0
for line_i, line in enumerate(data):
    x, y, z, r = [int(i) for i in re.search(re_str, line).groups()]

    new_point = np.array([x, y, z])
    if np.sum(np.abs(new_point - max_point)) <= max_r:
        count += 1

print(count)
