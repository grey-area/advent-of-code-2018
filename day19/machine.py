import operator
from functools import partial

    
class Machine():
    def __init__(self):
        self.ops = self.get_ops()
        self.registers = [0] * 6
        self.ip = 0
        self.ip_register = None
        self.program = []

    def step(self):
        pass

    def instruction(self, op, A_type, B_type, A, B):
        if A_type == 'r':
            A = self.registers[A]
        if B_type == 'r':
            B = self.registers[B]
        self.registers[C] = int(op(A, B))
        
    def get_ops(self):
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
            
        return ops
        

def load_data():
    with open('input') as f:
        program = f.read().splitlines()

    return program
