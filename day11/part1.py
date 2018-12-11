import numpy as np
from scipy.signal import convolve2d

INPUT = 7689

def cell_power(x, y):
    rack = x + 10
    power = (rack * y + INPUT) * rack
    power = (power % 1000) / 100 # hundreds digit
    return np.floor(power) - 5

power = np.fromfunction(cell_power, shape=(300, 300))
three_by_three = convolve2d(power, np.ones((3, 3)), mode='valid')

x, y = np.unravel_index(np.argmax(three_by_three), three_by_three.shape)
print(f'{x},{y}')
