import numpy as np

def get_type_grid(depth, target):
    W, H = target[0] + 100, target[1] + 100
    erosion_grid = np.zeros((W, H), dtype=np.int64)
    erosion_grid[0, 0] = depth % 20183
    erosion_grid[:, 0] = (np.arange(W) * 16807 + depth) % 20183
    erosion_grid[0, :] = (np.arange(H) * 48271 + depth) % 20183

    for i in range(1, W):
        for j in range(1, H):
            erosion_grid[i, j] = (erosion_grid[i-1, j] * erosion_grid[i, j-1] + depth) % 20183

    erosion_grid[target] = erosion_grid[0, 0]
    type_grid = erosion_grid % 3

    return type_grid
