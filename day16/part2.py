import re
from utils import get_ops, load_data

ops = get_ops()
examples, program = load_data()

# Record which ops are consistent with the behaviour observed for each opcode
opcode_consistent = {i: set(ops) for i in range(16)}
for example in examples:
    before_str, inst_str, after_str = example.splitlines()
    r = [int(i) for i  in re.findall('\d+', before_str)]
    opcode, A, B, C = [int(i) for i  in re.findall('\d+', inst_str)]
    target_r = [int(i) for i  in re.findall('\d+', after_str)]

    consistent = opcode_consistent[opcode]
    for op in consistent.copy():
        r1 = r.copy()
        op(A, B, C, r1)
        if r1 != target_r:
            consistent.remove(op)

# Once we've gone through all the examples, any op that is only consistent
# with a single opcode cannot be consistent with any other opcode.
# Repeatedly remove such ops from other opcodes.
opcodes = {}
while True:
    try:
        opcode, op_set = next((opcode, ops.copy()) for opcode, ops in opcode_consistent.items() if len(ops) == 1)
    except StopIteration:
        break

    opcodes[opcode] = next(iter(op_set))
    for consistent in opcode_consistent.values():
        consistent.difference_update(op_set)

# Run the program
r = [0, 0, 0, 0]
for line in program.splitlines():
    opcode, A, B, C = [int(i) for i  in re.findall('\d+', line)]
    opcodes[opcode](A, B, C, r)

print(r[0])
