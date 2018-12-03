import numpy as np
import re
import utils

# How many square inches belong to two or more claims?
# Regex the input.
# Store number of claims per square inch in a numpy array.


data = utils.load_data()

fabric = np.zeros((1000, 1000), dtype=np.int32)

for line in data:
    id_, x, y, w, h = map(int, re.search(utils.re_str, line).groups())

    fabric[y:y+h, x:x+w] += 1

print(np.sum(fabric > 1))
