from itertools import combinations

# Find the two strings that differ from each other in only 1 position.
# Use itertools.combinations to iterate over pairs of strings.
# Zip over pairs of characters, looking for differences.
# Used own argmax instead of numpy's to remind myself of max's
# key argument.


def argmax(ls):
    return max(range(len(line1)), key=lambda x: ls[x])


with open('input') as f:
    data = f.read().splitlines()
    
for line1, line2 in combinations(data, r=2):
    diffs = [c1 != c2 for c1, c2 in zip(line1, line2)]

    if sum(diffs) == 1:
        remove_index = argmax(diffs)
        print(line1[:remove_index] + line1[remove_index + 1:])
        break
