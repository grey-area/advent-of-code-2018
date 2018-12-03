from collections import namedtuple


def load_data():
    with open('input') as f:
        data = f.read().splitlines()
    return data


re_str = '^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$'

Claim = namedtuple('Claim', ['x', 'y', 'w', 'h'])
    

