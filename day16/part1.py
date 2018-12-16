import re
from utils import get_ops, load_data

ops = get_ops()
examples, program = load_data()

count = 0
for example in examples:
    before_str, inst_str, after_str = example.splitlines()
    r = [int(i) for i  in re.findall('\d+', before_str)]
    opcode, A, B, C = [int(i) for i  in re.findall('\d+', inst_str)]
    target_r = [int(i) for i  in re.findall('\d+', after_str)]

    consistent_ops = 0
    for op in ops:
        r1 = r.copy()
        op(A, B, C, r1)
        consistent_ops += (r1 == target_r)
    count += (consistent_ops >= 3)

print(count)
