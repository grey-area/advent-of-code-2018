import numpy as np
import re
from collections import defaultdict


class Cart():
    def __init__(self, x, y, vel):
        self.pos = np.array([x, y], dtype=np.int32)
        self.vel = vel
        self.mode = -1

    def take_corner(self, corner_type):
        self.vel = self.vel[::-1] * (-1)**corner_type

    def update(self, occupancy, junctions, corners):
        occupancy[tuple(self.pos)] -= 1
        self.pos += self.vel
        tuple_pos = tuple(self.pos)

        occupancy[tuple_pos] += 1

        for corner_type, corner_list in corners.items():
            if tuple_pos in corner_list:
                self.take_corner(corner_type)

        if tuple_pos in junctions:
            if self.mode != 0:
                corner_type = int((self.mode > 0) == (self.vel[0] == 0))
                self.take_corner(corner_type)
            self.mode = (self.mode + 2) % 3 - 1

        collision = occupancy[tuple_pos] > 1
        return collision


with open('input') as f:
    lines = f.read().replace('\\', '0').replace('/', '1').splitlines()

directions_str = '>v<^'
directions = [np.array(x) for x in [[1, 0], [0, 1], [-1, 0], [0, -1]]]
re_str = '>|v|<|\^|\+|0|1'
carts = []
junctions = []
corners = defaultdict(list)
M, N = len(lines[0]), len(lines)

for y, line in enumerate(lines):
    for element in re.finditer(re_str, line):
        x = element.span()[0]
        t = element.group()

        if t in directions_str:
            direction = directions[directions_str.index(t)]
            carts.append(Cart(x, y, direction))
        elif t=='+':
            junctions.append((x, y))
        else:
            corners[int(t)].append((x, y))

occupancy = np.zeros((M, N), dtype=np.int32)
for c in carts:
    occupancy[tuple(c.pos)] = 1

i = 0
while True:
    i += 1
    carts = sorted(carts, key=lambda c: (c.pos[1], c.pos[0]))
    for c in carts:
        collision = c.update(occupancy, junctions, corners)
        if collision:
            print(tuple(c.pos))
            break
    if collision:
        break
