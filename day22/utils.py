import numpy as np

def get_type_grid(depth, target):
    erosion_grid = -1 * np.ones((target[0] + 100, target[1] + 100), dtype=np.int64)
    erosion_grid[0, 0] = depth % 20183
    erosion_grid[:, 0] = np.fromfunction(lambda x: (16807 * x + depth) % 20183, (erosion_grid.shape[0], ))
    erosion_grid[0, :] = np.fromfunction(lambda y: (48271 * y + depth) % 20183, (erosion_grid.shape[1], ))

    for i in range(1, erosion_grid.shape[0]):
        for j in range(1, erosion_grid.shape[1]):
            erosion_grid[i, j] = (erosion_grid[i-1, j] * erosion_grid[i, j-1] + depth) % 20183

    erosion_grid[target] = erosion_grid[0, 0]
    type_grid = erosion_grid % 3

    return type_grid
