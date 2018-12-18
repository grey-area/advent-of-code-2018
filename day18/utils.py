import numpy as np
from scipy.signal import convolve

OPEN = 1
TREE = 9
LUMBER = 81
cell_type_values = [OPEN, TREE, LUMBER]
cell_types = '.|#'

def update(grid, kernel):
    adjacency_encoding = convolve(grid, kernel, mode='same')
    num_lumber, adjacency_encoding = np.divmod(adjacency_encoding, LUMBER)
    num_trees, num_open = np.divmod(adjacency_encoding, TREE)

    new_grid = np.copy(grid)
    new_grid[np.logical_and(grid==OPEN, num_trees >= 3)] = TREE
    new_grid[np.logical_and(grid==TREE, num_lumber >= 3)] = LUMBER
    new_grid[np.logical_and(grid==LUMBER, np.logical_or(num_trees==0, num_lumber==0))] = OPEN
    return new_grid

def load_data():
    with open('input') as f:
        data = f.read().splitlines()

    grid = np.array([[cell_type_values[cell_types.index(c)] for c in row] for row in data])

    kernel = np.ones((3, 3), dtype=np.int32)
    kernel[1, 1] = 0

    return grid, kernel
