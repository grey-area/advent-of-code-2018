from collections import Counter

# Find the number of entries that have two or three duplicate
# characters

with open('input') as f:
    data = f.read().splitlines()

num_twos = 0
num_threes = 0
    
for line in data:
    counts = Counter(line).values()

    if 2 in counts:
        num_twos += 1
    if 3 in counts:
        num_threes += 1

print(num_twos * num_threes)
