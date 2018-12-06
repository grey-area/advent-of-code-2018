from collections import namedtuple
import re

Point = namedtuple('Point', 'y x')
points = []

def load_data():
    with open('input') as f:
        data = f.read().splitlines()

    for line in data:
        p = Point(*map(int, re.search('^(\d+), (\d+)$', line).groups()))
        points.append(p)

    return points
