import numpy as np
from itertools import cycle

# Print the first frequency offset that occurs twice
# Done here by cycling round the array and storing seen values in a set
# Requires looping through the array 135 times

freq_changes = np.loadtxt('input', dtype=np.int32)

freq_seen = {0}
freq = 0
for change in cycle(freq_changes):
    freq += change
    if freq in freq_seen:
        break
    freq_seen.add(freq)

print(freq)
