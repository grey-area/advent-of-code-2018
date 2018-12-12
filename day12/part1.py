import re
import numpy as np
from scipy.signal import convolve

def transform(state, results, kernel):
    return results[convolve(state, kernel, mode='full')]

with open('input') as f:
    data = f.read().splitlines()

state_str = re.search(': (.+)$', data[0]).groups()[0]
state = np.array([1 if x=='#' else 0 for x in state_str])

results = np.zeros(32, dtype=np.int64)
for line in data[2:]:
    pattern, result = re.search('^(.+) => (.)$', line).groups()
    pattern_index = sum([2**(4-x_i) if x=='#' else 0 for x_i, x in enumerate(pattern)])
    results[pattern_index] = int(result=='#')
kernel = np.array([2**x_i for x_i in range(5)], dtype=np.int64)

steps = 20
for i in range(steps):
    state = transform(state, results, kernel)

first_index = -2 * steps
indices = np.arange(first_index, first_index + state.size, 1)

print(np.sum(indices * state))
