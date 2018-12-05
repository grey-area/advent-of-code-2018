# Reduce the string by removing pairs of adjacent letters that are the same but have
# different capitalization.
# Report the length of the resulting string.

def reduce(start_str):
    ans_str = []

    for c in start_str:
        if len(ans_str) > 0 and c != ans_str[-1] and c.lower() == ans_str[-1].lower():
            ans_str.pop()
        else:
            ans_str.append(c)

    return ''.join(ans_str)

if __name__=='__main__':
    with open('input') as f:
        data = f.read().strip('\n')

    print(len(reduce(data)))
