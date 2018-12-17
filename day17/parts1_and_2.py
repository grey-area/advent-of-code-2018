import re
import numpy as np

with open('input') as f:
    data = f.read().splitlines()

x_min = 1000000
x_max = 0
y_min = 1000000
y_max = 0

for line in data:
    if line == '':
        continue
    u, d1, d2 = [int(i) for i in re.search('=(\d+), \D=(\d+)..(\d+)', line).groups()]
    if line[0] == 'x':
        x_min = min(x_min, u)
        x_max = max(x_max, u)
        y_min = min(y_min, d1)
        y_max = max(y_max, d2)
    else:
        x_min = min(x_min, d1)
        x_max = max(x_max, d2)
        y_min = min(y_min, u)
        y_max = max(y_max, u)

x_min -= 2
x_max += 2

grid = np.zeros((y_max + 1, x_max - x_min + 1), dtype=np.int32)

for line in data:
    if line == '':
        continue
    u, d1, d2 = [int(i) for i in re.search('=(\d+), \D=(\d+)..(\d+)', line).groups()]
    if line[0] == 'x':
        grid[d1:d2 + 1, -x_min + u] = 3
    else:
        grid[u, -x_min + d1:-x_min + d2 + 1] = 3


def search_horizontal(grid, x0, y0, y_max):
    xl, xr, y = x0, x0, y0
    while grid[y, xl] < 2 and grid[y + 1, xl] in [2, 3]:
        xl -= 1
    while grid[y, xr] < 2 and grid[y + 1, xr] in [2, 3]:
        xr += 1

    if grid[y, xl] == 3 and grid[y, xr] == 3:
        xl += 1
        grid[y, xl:xr] = 2
        search_horizontal(grid, x0, y0-1, y_max)
    else:
        grid[y, xl+1:xr] = 1
        if grid[y, xr] < 2:
            search_vertical(grid, xr, y, y_max)
        if grid[y, xl] < 2:
            search_vertical(grid, xl, y, y_max)

# Go straight down til you hit clay or water
# Search horizontally in both directions until you hit clay
# If you do hit clay, fill in the row, start the search again one row up
# If you don't hit clay at either end, start the search again at both ends
def search_vertical(grid, x0, y0, y_max):
    x, y = x0, y0
    saw = False
    while grid[y, x] < 2 and y < y_max:
        y += 1
        if grid[y, x] == 1:
            saw = True

    grid[y0:y, x] = 1
    if y == y_max and grid[y, x] < 2:
        grid[y, x] = 1

    if y == y_max and grid[y, x] < 2:
        return
    if saw:
        return

    y -= 1
    search_horizontal(grid, x, y, y_max)

search_vertical(grid, 500 - x_min, 0, y_max)
grid = grid[y_min:, :]
print(np.sum(np.logical_or(grid==1, grid==2)))
print(np.sum(grid==2))
