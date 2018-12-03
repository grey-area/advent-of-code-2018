import numpy as np
import re

# How many square inches belong to two or more claims?
# Regex the input.
# Store number of claims per square inch in a numpy array.


with open('input') as f:
    data = f.read().splitlines()
re_str = '^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$'
    
fabric = np.zeros((1000, 1000), dtype=np.int32)

for line in data:
    id_, x, y, w, h = [int(s) for s in re.search(re_str, line).groups()]
    
    fabric[y:y+h, x:x+w] += 1

print(np.sum(fabric > 1))
    
