import re
import sys
import numpy as np


class Lights():
    def __init__(self, x, y, v_x, v_y):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y

        self.size = sys.maxsize
        self.compute_size()

    def update(self, sign=1):
        self.x += sign * self.v_x
        self.y += sign * self.v_y

    def compute_size(self):
        min_x = np.min(self.x)
        max_x = np.max(self.x)
        min_y = np.min(self.y)
        max_y = np.max(self.y)

        self.prev_size = self.size
        self.size = (max_x - min_x) * (max_y - min_y)


def load_data():
    with open('input') as f:
        data = f.read().splitlines()

    re_str = '^position=< *(-?\d+), *(-?\d+)> velocity=< *(-?\d+), *(-?\d+)>$'

    x = np.zeros(len(data))
    y = np.zeros(len(data))
    v_x = np.zeros(len(data))
    v_y = np.zeros(len(data))

    for line_i, line in enumerate(data):
        x[line_i], y[line_i], v_x[line_i], v_y[line_i] = map(int, re.search(re_str, line).groups())

    lights = Lights(x, y, v_x, v_y)

    return lights
