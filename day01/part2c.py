import numpy as np

# Print the first frequency offset that occurs twice
# Done by storing the frequencies seen during the first cycle,
# then incrementing by first cycle final frequency looking for a repeat.
# Any repeat must be a repeat of a frequency seen during the first cycle.
# About 3x faster than adding every frequency seen to a set and checking membership.

freq_changes = np.loadtxt('input', dtype=np.int32)
initial_cycle = np.cumsum(freq_changes)

current_cycle = np.copy(initial_cycle)
while True:
    current_cycle += initial_cycle[-1]
    membership = np.in1d(current_cycle, initial_cycle)
    if np.any(membership):
        print(current_cycle[membership][0])
        break

