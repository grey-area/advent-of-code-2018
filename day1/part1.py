import numpy as np

# Print the total offset by the end of the list

frequency_changes = np.loadtxt('input', dtype=np.int32)

print(np.sum(frequency_changes))
