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

# Record which ops are consistent with the behaviour observed for each opcode
opcode_consistent = {i: set(ops) for i in range(16)}

for example in examples:
    before_str, inst_str, after_str = example.splitlines()
    r0 = [int(i) for i  in re.findall('\d+', before_str)]
    opcode, A, B, C = [int(i) for i  in re.findall('\d+', inst_str)]
    target_r1 = [int(i) for i  in re.findall('\d+', after_str)]

    consistent = opcode_consistent[opcode]
    for op in consistent.copy():
        r1 = r0.copy()
        op(A, B, C, r1)
        if r1 != target_r1:
            consistent.remove(op)

for i in range(16):
    for opcode in range(16):
        if len(opcode_consistent[opcode]) == 1:
            op = next(iter(opcode_consistent[opcode]))
            for opcode1 in range(16):
                if opcode1 == opcode or op not in opcode_consistent[opcode1]:
                    continue
                opcode_consistent[opcode1].remove(op)

opcodes = [next(iter(opcode_consistent[opcode])) for opcode in range(16)]
r = [0, 0, 0, 0]
for line in part2[1:].splitlines():
    opcode, A, B, C = [int(i) for i  in re.findall('\d+', line)]
    opcodes[opcode](A, B, C, r)

print(r[0])
