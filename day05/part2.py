from string import ascii_lowercase
import re

# For each letter, remove all instances of that letter in each case.
# Then reduce the string by removing pairs of adjacent letters that are the same but have
# different capitalization.
# Report the length of the shortest resulting string.

with open('input') as f:
    data = f.read().strip('\n')

resulting_lengths = {}

for l in ascii_lowercase:
    data_rem_l = re.sub(f'{l}|{l.upper()}', '', data)

    ans_str = []

    for c in data_rem_l:
        if len(ans_str) > 0 and c != ans_str[-1] and c.lower() == ans_str[-1].lower():
            ans_str.pop()
        else:
            ans_str.append(c)

    resulting_lengths[l] = len(ans_str)

print(min(resulting_lengths.values()))
