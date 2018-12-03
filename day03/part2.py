import numpy as np
import re
from collections import namedtuple

# How many square inches belong to two or more claims?
# Regex the input.
# Store number of claims per square inch in a numpy array.
# Then check for each claim whether the number of square inches
# claimed within its area is equal to its area.


with open('input') as f:
    data = f.read().splitlines()
re_str = '^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$'


Claim = namedtuple('Claim', ['x', 'y', 'w', 'h'])
claims = {}


fabric = np.zeros((1000, 1000), dtype=np.int32)

for line in data:
    id_, x, y, w, h = map(int, re.search(re_str, line).groups())
    claims[id_] = Claim(x, y, w, h)

    fabric[y:y+h, x:x+w] += 1


for id_, c in claims.items():
    if np.sum(fabric[c.y:c.y+c.h, c.x:c.x+c.w]) == c.w * c.h:
        print(id_)
        break
