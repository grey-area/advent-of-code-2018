import operator
from functools import partial
import re


class Machine():
    def __init__(self):
        self.set_ops()
        self.registers = [0] * 6
        self.ip = 0
        self.load_program()

    def step(self):
        self.registers[self.ip_register] = self.ip

        if self.ip < 0 or self.ip >= len(self.program):
            return 'halt'

        op, opargs = self.program[self.ip]
        op(*opargs)
        self.ip = self.registers[self.ip_register]
        self.ip += 1

    def instruction(self, op, A_type, B_type, A, B, C):
        if A_type == 'r':
            A = self.registers[A]
        if B_type == 'r':
            B = self.registers[B]
        self.registers[C] = int(op(A, B))

    def set_ops(self):
        ops = {}
        for opname, op in zip(['add', 'mul', 'ban', 'bor'],
                              [operator.add, operator.mul, operator.and_, operator.or_]):
            for optype in ['r', 'i']:
                ops[opname + optype] = partial(self.instruction, op, 'r', optype)
        for optype in ['r', 'i']:
            ops['set' + optype] = partial(self.instruction, lambda a, b: a, optype, None)
        for opname, op in zip(['gt', 'eq'],
                              [operator.gt, operator.eq]):
            ops[opname + 'ir'] = partial(self.instruction, op, 'i', 'r')
            ops[opname + 'ri'] = partial(self.instruction, op, 'r', 'i')
            ops[opname + 'rr'] = partial(self.instruction, op, 'r', 'r')

        self.ops = ops

    def load_program(self):
        with open('input') as f:
            data = f.read().splitlines()

        self.ip_register = int(re.search('\d', data[0]).group())

        self.program = []
        for line in data[1:]:
            inst = line.split(' ')
            op = self.ops[inst[0]]
            opargs = [int(i) for i in inst[1:]]
            self.program.append((op, opargs))
