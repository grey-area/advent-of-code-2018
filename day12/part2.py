import re
import numpy as np
from scipy.signal import convolve, fftconvolve

def transform(state, results, kernel):
    index_offset = 0

    if np.sum(state[:2]) > 0:
        state = np.concatenate((np.zeros(2, dtype=np.bool), state))
        index_offset -= 2
    if np.sum(state[-2:]) > 0:
        state = np.concatenate((state, np.zeros(2, dtype=np.bool)))

    indices = convolve(state, kernel, mode='same')
    state = results[indices]

    first_non_zero = np.argmax(state)
    if first_non_zero > 2:
        state = state[first_non_zero-2:]
        index_offset += first_non_zero - 2

    return state, index_offset

with open('input') as f:
    data = f.read().splitlines()

state_str = re.search(': (.+)$', data[0]).groups()[0]
state = np.array([1 if x=='#' else 0 for x in state_str])

results = np.zeros(32, dtype=np.bool)
for line in data[2:]:
    pattern, result = re.search('^(.+) => (.)$', line).groups()
    pattern_index = sum([2**(4-x_i) if x=='#' else 0 for x_i, x in enumerate(pattern)])
    results[pattern_index] = int(result=='#')
kernel = np.array([2**x_i for x_i in range(5)], dtype=np.int8)

seen_states = [state.copy()]
seen_offsets = [0]

first_index = 0
steps = 50000000000
terminate = False
for i in range(1, steps, 1):
    state, index_offset = transform(state, results, kernel)
    first_index += index_offset

    for state_i, (seen_state, seen_offset) in enumerate(zip(seen_states, seen_offsets)):
        if state.size == seen_state.size and np.all(state == seen_state):
            terminate = True
            print(first_index, seen_offset, i, state_i)

    if terminate:
        break

    seen_states.append(state)
    seen_offsets.append(first_index)

iteration_diff = i - state_i
index_diff = first_index - seen_offset

first_index += ((steps - i) // iteration_diff) * index_diff

indices = np.arange(first_index, first_index + state.size, 1)
print(np.sum(indices * state))
