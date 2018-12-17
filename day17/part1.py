import re
import numpy as np

SAND = 0
WATER_FLOW = 1
WATER = 2
CLAY = 3

with open('input') as f:
    data = f.read().splitlines()

xs = []
ys = []
for line in data:
    u, d1, d2 = [int(i) for i in re.search('=(\d+), \D=(\d+)..(\d+)', line).groups()]
    if line[0] == 'x':
        xs.append(u)
        ys += [d1, d2]
    else:
        xs += [d1, d2]
        ys.append(u)

x_min = np.min(xs) - 1
x_max = np.max(xs) + 1
y_min, y_max = np.min(ys), np.max(ys)
grid = np.zeros((y_max + 1, x_max - x_min + 1), dtype=np.int32)

for line in data:
    u, d1, d2 = [int(i) for i in re.search('=(\d+), \D=(\d+)..(\d+)', line).groups()]
    if line[0] == 'x':
        grid[d1:d2 + 1, -x_min + u] = CLAY
    else:
        grid[u, -x_min + d1:-x_min + d2 + 1] = CLAY


def search_horizontal(grid, x0, y0, y_max):
    xl, xr, y = x0, x0, y0
    while grid[y, xl] in [SAND, WATER_FLOW] and grid[y + 1, xl] in [WATER, CLAY]:
        xl -= 1
    while grid[y, xr] in [SAND, WATER_FLOW] and grid[y + 1, xr] in [WATER, CLAY]:
        xr += 1

    if grid[y, xl] == grid[y, xr] == CLAY:
        xl += 1
        grid[y, xl:xr] = WATER
        search_horizontal(grid, x0, y0-1, y_max)
    else:
        grid[y, xl+1:xr] = WATER_FLOW
        if grid[y, xr] in [SAND, WATER_FLOW]:
            search_vertical(grid, xr, y, y_max)
        if grid[y, xl] in [SAND, WATER_FLOW]:
            search_vertical(grid, xl, y, y_max)


# Go straight down til you hit clay or water
# Search horizontally in both directions until you hit clay
# If you do hit clay, fill in the row, start the search again one row up
# If you don't hit clay at either end, start the search again at both ends
def search_vertical(grid, x, y0, y_max):
    y = y0
    saw = False
    while grid[y, x] in [SAND, WATER_FLOW] and y < y_max:
        y += 1
        if grid[y, x] == WATER_FLOW:
            saw = True

    grid[y0:y, x] = WATER_FLOW
    if y == y_max and grid[y, x] in [SAND, WATER_FLOW]:
        grid[y, x] = WATER_FLOW

    if y == y_max and grid[y, x] in [SAND, WATER_FLOW]:
        return
    if saw:
        return

    y -= 1
    search_horizontal(grid, x, y, y_max)


search_vertical(grid, 500 - x_min, 0, y_max)
grid = grid[y_min:, :]
print(np.sum(np.logical_or(grid==WATER_FLOW, grid==WATER)))
print(np.sum(grid==WATER))
