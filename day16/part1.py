import re
from utils import get_ops, load_data

ops = get_ops()
part1, part2 = load_data()

count = 0
for example in part1:
    before_str, inst_str, after_str = example.splitlines()
    r0 = [int(i) for i  in re.findall('\d+', before_str)]
    opcode, A, B, C = [int(i) for i  in re.findall('\d+', inst_str)]
    target_r1 = [int(i) for i  in re.findall('\d+', after_str)]

    consistent_ops = 0
    for op in ops:
        r1 = r0.copy()
        op(A, B, C, r1)
        consistent_ops += (r1 == target_r1)
    count += (consistent_ops >= 3)

print(count)
