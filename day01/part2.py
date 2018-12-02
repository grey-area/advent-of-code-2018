import numpy as np
from itertools import cycle

# Print the first frequency offset that occurs twice
# Done by storing the frequencies seen during the first cycle,
# then cycling round the array looking for a reoccurance.
# Any repeat must be a repeat of a frequency seen during the first cycle.
# Requires looping through the array 135 times

freq_changes = np.loadtxt('input', dtype=np.int32)
initial_cycle = np.cumsum(freq_changes)

freq = initial_cycle[-1]
initial_cycle = frozenset(initial_cycle)
for change in cycle(freq_changes):
    freq += change
    if freq in initial_cycle:
        print(freq)
        break
