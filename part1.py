import numpy as np
from scipy.signal import convolve

with open('example_input') as f:
    data = f.read().splitlines()

OPEN = 0
TREES = 9
LUMBER = 81
cell_type_values = [OPEN, TREES, LUMBER]
cell_types = '.|#'

def update(grid, kernel):
    result = convolve(grid, kernel, mode='same')
    print(grid.shape)
    print(result.shape)
    print(grid)
    print(result)

grid = np.array([[cell_type_values[cell_types.index(c)] for c in row] for row in data])

kernel = np.ones((3, 3), dtype=np.int32)
kernel[1, 1] = 0

update(grid, kernel)
