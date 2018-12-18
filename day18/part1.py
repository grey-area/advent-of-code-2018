import numpy as np
import utils
from utils import TREE, LUMBER

grid, kernel = utils.load_data()

for i in range(10):
    grid = utils.update(grid, kernel)

print(np.sum(grid==TREE) * np.sum(grid==LUMBER))
