import utils
import time
import matplotlib.pyplot as plt

lights = utils.load_data()

while lights.size < lights.prev_size:
    lights.update()
    lights.compute_size()
lights.update(-1)

plt.scatter(lights.x, -lights.y)
plt.show()
