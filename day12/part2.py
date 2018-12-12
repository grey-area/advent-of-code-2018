import re
import numpy as np
from scipy.signal import convolve, fftconvolve


def transform(state, kernel, rules):
    index_offset = 0

    # Ensure that the state has at least 2 leading and trailing empty pots
    # and adjust index offset
    if np.sum(state[:2]) > 0:
        state = np.concatenate((np.zeros(2, dtype=np.bool), state))
        index_offset -= 2
    if np.sum(state[-2:]) > 0:
        state = np.concatenate((state, np.zeros(2, dtype=np.bool)))

    # Iterate
    state = rules[convolve(state, kernel, mode='same')]

    # Strip off leading empty pots and adjust index offset
    first_non_zero = np.argmax(state)
    state = state[first_non_zero:]
    index_offset += first_non_zero

    # Strip off trailing empty pots
    last_non_zero = state.size - np.argmax(state[::-1]) + 1
    state = state[:last_non_zero]

    return state, index_offset


def load_data():
    with open('input') as f:
        data = f.read().splitlines()

    state_str = re.search(': (.+)$', data[0]).groups()[0]
    state = np.array([1 if x=='#' else 0 for x in state_str])

    rules = np.zeros(32, dtype=np.bool)
    for line in data[2:]:
        pattern, result = re.search('^(.+) => (.)$', line).groups()
        pattern_index = sum([2**(4-x_i) if x=='#' else 0 for x_i, x in enumerate(pattern)])
        rules[pattern_index] = int(result=='#')

    return state, rules


def main():
    state, rules = load_data()
    kernel = np.array([2**x_i for x_i in range(5)], dtype=np.int8)

    # Record states that we've seen before, and the index of the
    seen_states = [state.copy()]
    seen_index_offsets = [0]

    index_offset = 0
    steps = 50000000000
    terminate = False
    for i in range(1, steps, 1):
        state, index_offset_change = transform(state, kernel, rules)
        index_offset += index_offset_change

        for state_i, (seen_state, seen_offset) in enumerate(zip(seen_states, seen_index_offsets)):
            if state.size == seen_state.size and np.all(state == seen_state):
                terminate = True

        if terminate:
            break

        seen_states.append(state)
        seen_index_offsets.append(index_offset)

    iteration_diff = i - state_i
    index_diff = index_offset - seen_offset

    index_offset += ((steps - i) // iteration_diff) * index_diff

    indices = np.arange(index_offset, index_offset + state.size, 1)
    print(np.sum(indices * state))


if __name__ == '__main__':
    main()
