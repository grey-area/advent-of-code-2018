from utils import get_type_grid

depth = 3066
target = (13, 726)

type_grid = get_type_grid(depth, target)

print(type_grid[:target[0] + 1, :target[1] + 1].sum())
