import operator
from functools import partial

def instruction(op, A_type, B_type, A, B, C, registers):
    if A_type == 'r':
        A = registers[A]
    if B_type == 'r':
        B = registers[B]
    registers[C] = int(op(A, B))

# Build the set of ops
def get_ops():
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
    return ops

def load_data():
    with open('input') as f:
        text = f.read()
        part1, part2 = text.split('\n\n\n')

    return part1.split('\n\n'), part2[1:]
