# Reduce the string by removing pairs of adjacent letters that are the same but have
# different capitalization.
# Report the length of the resulting string.

with open('input') as f:
    data = f.read().strip('\n')

ans_str = []

for c in data:
    if len(ans_str) > 0 and c != ans_str[-1] and c.lower() == ans_str[-1].lower():
        ans_str.pop()
    else:
        ans_str.append(c)

print(len(ans_str))
