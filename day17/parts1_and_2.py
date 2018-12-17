import re
import numpy as np


SAND = 0
WATER_FLOW = 1
WATER = 2
CLAY = 3


def load_data():
    with open('input') as f:
        data = f.read().splitlines()
    re_str = '=(\d+), \D=(\d+)..(\d+)'
    xs = []
    ys = []
    for line in data:
        u, d1, d2 = [int(i) for i in re.search(re_str, line).groups()]
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
        u, d1, d2 = [int(i) for i in re.search(re_str, line).groups()]
        if line[0] == 'x':
            grid[d1:d2 + 1, -x_min + u] = CLAY
        else:
            grid[u, -x_min + d1:-x_min + d2 + 1] = CLAY

    return x_min, y_min, y_max, grid


def search_horizontal(grid, x0, y, y_max):
    xl = xr = x0
    while grid[y, xl] in [SAND, WATER_FLOW] and grid[y + 1, xl] in [WATER, CLAY]:
        xl -= 1
    while grid[y, xr] in [SAND, WATER_FLOW] and grid[y + 1, xr] in [WATER, CLAY]:
        xr += 1

    if grid[y, xl] == grid[y, xr] == CLAY:
        xl += 1
        grid[y, xl:xr] = WATER
        search_horizontal(grid, x0, y-1, y_max)
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
    prev_visited = False

    while grid[y, x] in [SAND, WATER_FLOW] and y < y_max:
        y += 1
        if grid[y, x] == WATER_FLOW:
            prev_visited = True

    grid[y0:y, x] = WATER_FLOW
    if y == y_max and grid[y, x] == SAND:
        grid[y, x] = WATER_FLOW

    if prev_visited:
        return

    y -= 1
    search_horizontal(grid, x, y, y_max)


if __name__ == '__main__':
    x_min, y_min, y_max, grid = load_data()
    search_vertical(grid, 500 - x_min, 0, y_max)
    grid = grid[y_min:, :]
    print('Part 1: ', np.sum(np.logical_or(grid==WATER_FLOW, grid==WATER)))
    print('Part 2: ', np.sum(grid==WATER))
