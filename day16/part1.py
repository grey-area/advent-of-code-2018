import operator
from functools import partial
import re

def instruction(op, A_type, B_type, A, B, C, registers):
    if A_type == 'r':
        A = registers[A]
    if B_type == 'r':
        B = registers[B]
    registers[C] = int(op(A, B))

# Build the set of ops
ops = []
for op in [operator.add, operator.mul, operator.and_, operator.or_]:
    ops.append(partial(instruction, op, 'r', 'r'))
    ops.append(partial(instruction, op, 'r', 'i'))
ops.append(partial(instruction, lambda a, b: a, 'r', None))
ops.append(partial(instruction, lambda a, b: a, 'i', None))
for op in [operator.gt, operator.eq]:
    ops.append(partial(instruction, op, 'i', 'r'))
    ops.append(partial(instruction, op, 'r', 'i'))
    ops.append(partial(instruction, op, 'r', 'r'))

with open('input') as f:
    text = f.read()
    part1, part2 = text.split('\n\n\n')
    examples = part1.split('\n\n')

count = 0
for example in examples:
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
