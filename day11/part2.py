import numpy as np
from scipy.signal import fftconvolve

INPUT = 7689

def cell_power(x, y):
    rack = x + 10
    power = (rack * y + INPUT) * rack
    power = (power % 1000) / 100 # hundreds digit
    return np.floor(power) - 5

def compute_max_coord(power, kernel):
    convolved = fftconvolve(power, np.ones((kernel, kernel)), mode='valid')
    index = np.argmax(convolved)
    value = convolved.flat[index]
    coords = np.unravel_index(index, convolved.shape)
    return coords, value

power = np.fromfunction(cell_power, shape=(300, 300))

print(max([(k, compute_max_coord(power, k)) for k in range(1, 301)], key=lambda x: x[1][1]))
