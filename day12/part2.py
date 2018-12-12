import re
import numpy as np
from scipy.signal import convolve, fftconvolve


# Principle: in order to feasibly compute the answer for the 50 billionth iteration,
# the automata has to reach some kind of steady state, though the fixed pattern may move
# to the left or right.
# After each iteration, we strip off leading and trailing empty pots. We record the current pattern,
# the iteration at which it happened, and the index of the left-most pot.
# We look for the first pattern that repeats at two iterations. We use the difference between
# the two iterations and the difference between the index of the left-most pot in the two
# iterations to extrapolate the index of the left-most pot by the Nth iteration, and
# then compute the result


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

    # Record states that we've seen before, the iteration at which we saw them,
    # and the index of the left-most pot when we saw them
    seen_states = {state.tobytes(): (0, 0)}

    N = 50000000000
    index_offset = 0

    for iteration in range(1, N, 1):
        state, index_offset_change = transform(state, kernel, rules)
        index_offset += index_offset_change

        state_bytes = state.tobytes() # hashable
        # If we've seen this state before, record the iteration at which it happened
        # and the index of the left-most pot at that iteration
        if state_bytes in seen_states.keys():
            seen_iteration, seen_offset = seen_states[state_bytes]
            break

        seen_states[state_bytes] = (iteration, index_offset)

    # Adjust the index offset to what it would be by the Nth step
    iteration_diff = iteration - seen_iteration
    index_diff = index_offset - seen_offset
    index_offset += ((N - iteration) // iteration_diff) * index_diff

    # Compute the indices of the pots for the Nth step
    indices = np.arange(index_offset, index_offset + state.size, 1)
    # Compute the sum of indices of pots with plants for the Nth step
    print(np.sum(indices * state))


if __name__ == '__main__':
    main()
