import numpy as np

# Print the first frequency offset that occurs twice
# Done here by recording the frequency offset after having seen every change in the array
# by computing the cumulative sum, and then computing the NxN array of differences between
# each element of the offset array and each other element.
# We then look for the smallest non-zero difference that is divisible by the total
# frequency offset per cycle of the frequency change array, and is the same sign as that
# total change.

# This approach is ~4x faster than cycling through the array looking for repeats.

freq_changes = np.loadtxt('input', dtype=np.int32)

first_cycle_freqs = np.cumsum(freq_changes)
final_offset = first_cycle_freqs[-1]
sign = 1

if final_offset < 0:
    first_cycle_freqs *= -1
    final_offset *= -1
    sign = -1

diffs = np.expand_dims(first_cycle_freqs, axis=0) - np.expand_dims(first_cycle_freqs, axis=1)
divisible = np.logical_and(diffs > 0, diffs % final_offset == 0)
divisible_indices = np.argwhere(divisible)

ans = first_cycle_freqs[divisible_indices[np.argmin(diffs[divisible]), 1]]    
print(sign * ans)

