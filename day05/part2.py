from string import ascii_lowercase
import re
import part1

# For each letter, remove all instances of that letter in each case.
# Then reduce the string by removing pairs of adjacent letters that are the same but have
# different capitalization.
# Report the length of the shortest resulting string.

with open('input') as f:
    data = f.read().strip('\n')

# Note, we can reduce the string *before* trialing removing each letter and further reducing
data = part1.reduce(data)

resulting_lengths = {}

for l in ascii_lowercase:
    data_rem_l = re.sub(f'{l}|{l.upper()}', '', data)

    resulting_lengths[l] = len(part1.reduce(data_rem_l))

print(min(resulting_lengths.values()))
