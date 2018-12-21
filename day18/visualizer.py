import numpy as np
from scipy.signal import convolve
import time

with open('input') as f:
    data = f.read().splitlines()

OPEN = 1
TREE = 9
LUMBER = 81
cell_type_values = [OPEN, TREE, LUMBER]
cell_types = '.|#'

def print_grid(grid):
    ans_str = '\n'
    for i in range(grid.shape[0]):
        ans_str += '\n' + ''.join(cell_types[cell_type_values.index(c)] for c in grid[i, :])

    print(ans_str)

def update(grid, kernel):
    adjacency_encoding = convolve(grid, kernel, mode='same')
    num_lumber, adjacency_encoding = np.divmod(adjacency_encoding, LUMBER)
    num_trees, num_open = np.divmod(adjacency_encoding, TREE)

    new_grid = np.copy(grid)
    new_grid[np.logical_and(grid==OPEN, num_trees >= 3)] = TREE
    new_grid[np.logical_and(grid==TREE, num_lumber >= 3)] = LUMBER
    new_grid[np.logical_and(grid==LUMBER, np.logical_or(num_trees==0, num_lumber==0))] = OPEN
    return new_grid

grid = np.array([[cell_type_values[cell_types.index(c)] for c in row] for row in data])

kernel = np.ones((3, 3), dtype=np.int32)
kernel[1, 1] = 0

for i in range(1000000):
    print(chr(27) + "[2J")
    grid = update(grid, kernel)
    print_grid(grid)
    time.sleep(0.03)
