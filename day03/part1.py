import numpy as np
import utils

# How many square inches belong to two or more claims?
# Regex the input.
# Store number of claims per square inch in a numpy array.


claims = utils.load_data()
fabric = np.zeros((1000, 1000), dtype=np.int32)

for c in claims.values():
    fabric[c.y:c.y+c.h, c.x:c.x+c.w] += 1

print(np.sum(fabric > 1))
