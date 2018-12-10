import utils
import time
import matplotlib.pyplot as plt

lights = utils.load_data()

s = 0
while lights.size < lights.prev_size:
    lights.update()
    lights.compute_size()
    s += 1
s -= 1

print(s)
