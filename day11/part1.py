import numpy as np
from scipy.signal import convolve2d

INPUT = 7689

rack = np.expand_dims(np.arange(300) + 10, axis=1)
ys = np.expand_dims(np.arange(300), axis=0)
power = (np.mod((rack * ys + INPUT) * rack, 1000) / 100).astype(np.int32) - 5

three_by_three = convolve2d(power, np.ones((3, 3)), mode='valid')

print(np.unravel_index(np.argmax(three_by_three), three_by_three.shape))
