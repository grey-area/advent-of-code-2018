from itertools import combinations

# Find the two strings that differ from each other in only 1 position.
# Use itertools.combinations to iterate over pairs of strings.
# Zip over pairs of characters, recording indices of differences.


with open('input') as f:
    data = f.read().splitlines()
    
for l1, l2 in combinations(data, r=2):
    diff_indices = [c_i for c_i, (c1, c2) in enumerate(zip(l1, l2)) if c1 != c2]

    if len(diff_indices) == 1:
        print(l1[:diff_indices[0]] + l1[diff_indices[0] + 1:])
        break
