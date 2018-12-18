import numpy as np
from collections import defaultdict
import utils
from utils import TREE, LUMBER

grid, kernel = utils.load_data()

seen_states = defaultdict(list)
period = None
M = 1000000000

for i in range(1, M + 1, 1):
    grid = utils.update(grid, kernel)
    ans = np.sum(grid==TREE) * np.sum(grid==LUMBER)

    if period is None:
        for j, prev_state in seen_states[ans]:
            if np.all(grid==prev_state):
                period = i - j
        seen_states[ans].append((i, grid))
    if period is not None and (M - i) % period == 0:
        break

print(ans)
