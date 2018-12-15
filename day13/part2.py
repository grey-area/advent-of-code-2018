import numpy as np
import re
from collections import defaultdict


class Cart():
    def __init__(self, x, y, vel):
        self.pos = np.array([x, y], dtype=np.int32)
        self.vel = vel
        self.mode = -1
        self.killed = False

    def take_corner(self, corner_type):
        self.vel = self.vel[::-1] * (-1)**corner_type

    def update(self, occupancy, junctions, corners):
        if self.killed:
            return set()

        x, y = self.pos
        occupancy[x][y].remove(self)
        self.pos += self.vel
        x, y = self.pos
        occupancy[x][y].add(self)

        for corner_type, corner_list in corners.items():
            if (x, y) in corner_list:
                self.take_corner(corner_type)

        if (x, y) in junctions:
            if self.mode != 0:
                corner_type = int((self.mode > 0) == (self.vel[0] == 0))
                self.take_corner(corner_type)
            self.mode = (self.mode + 2) % 3 - 1

        return occupancy[x][y]


with open('input') as f:
    lines = f.read().replace('\\', '0').replace('/', '1').splitlines()

directions_str = '>v<^'
directions = [np.array(x) for x in [[1, 0], [0, 1], [-1, 0], [0, -1]]]
re_str = '>|v|<|\^|\+|0|1'
carts = set()
junctions = set()
corners = defaultdict(set)
M, N = len(lines[0]), len(lines)

for y, line in enumerate(lines):
    for element in re.finditer(re_str, line):
        x = element.span()[0]
        t = element.group()

        if t in directions_str:
            direction = directions[directions_str.index(t)]
            carts.add(Cart(x, y, direction))
        elif t=='+':
            junctions.add((x, y))
        else:
            corners[int(t)].add((x, y))

occupancy = [[set() for j in range(N)] for i in range(M)]
for c in carts:
    x, y = c.pos
    occupancy[x][y].add(c)

collision=False
while True:
    carts_list = sorted(carts, key=lambda c: (c.pos[1], c.pos[0]))
    if len(carts_list) == 1:
        print(carts_list[0].pos)
        break

    for c in carts_list:
        cell_occupancy = c.update(occupancy, junctions, corners)
        if len(cell_occupancy) > 1:
            for c1 in cell_occupancy:
                c1.killed = True
                carts.remove(c1)
            cell_occupancy.clear()
