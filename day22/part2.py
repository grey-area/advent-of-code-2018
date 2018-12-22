from utils import get_type_grid
from dijkstar import Graph, find_path

depth = 3066
target = (13, 726)

type_grid = get_type_grid(depth, target)

# No gear equipped allows us to use wet (1) or narrow (2) regions
# Climbing gear allows us to use rocky (0) or wet (1) regions
# Torch allows us to use rocky (0) or narrow (2) regions
ROCK = 0
WET = 1
NARROW = 2

NO_GEAR = 0
CLIMBING = 1
TORCH = 2

equipment_per_terrain = {
    ROCK: set([CLIMBING, TORCH]),
    WET: set([NO_GEAR, CLIMBING]),
    NARROW: set([NO_GEAR, TORCH])
}

# For each position and equipment type equipped, we need a unique node ID for our graph
def node_id(equip, i, j, W, H):
    return equip * H * W + i * H + j

graph = Graph()
W, H = type_grid.shape

# Add edges to the graph with cost 1 for adjacent nodes when the
# appropriate equipment is equipped
for i in range(type_grid.shape[0] - 1):
    for j in range(type_grid.shape[1] - 1):
        for i1, j1 in [(i + 1, j), (i, j + 1)]:
            valid_equipment = equipment_per_terrain[type_grid[i, j]].intersection(equipment_per_terrain[type_grid[i1, j1]])
            for equip in valid_equipment:
                id1 = node_id(equip, i, j, W, H)
                id2 = node_id(equip, i1, j1, W, H)
                graph.add_edge(id1, id2, edge=1)
                graph.add_edge(id2, id1, edge=1)

# Add edges to the graph with cost 7 for swapping between the two
# allowed types of equipment in each position
for i in range(type_grid.shape[0]):
    for j in range(type_grid.shape[1]):
        equip1, equip2 = list(equipment_per_terrain[type_grid[i, j]])
        id1 = node_id(equip1, i, j, W, H)
        id2 = node_id(equip2, i, j, W, H)
        graph.add_edge(id1, id2, edge=7)
        graph.add_edge(id2, id1, edge=7)

# Use Dijkstra's algorithm to find the minimum cost path from the
# entrance of the cave with a torch equipped to the target with a torch
# equipped.
start_node = node_id(TORCH, 0, 0, W, H)
target_node = node_id(TORCH, target[0], target[1], W, H)
print(find_path(graph, start_node, target_node).total_cost)
