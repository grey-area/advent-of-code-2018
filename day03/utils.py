from collections import namedtuple
import re


def load_data():
    with open('input') as f:
        data = f.read().splitlines()

    Claim = namedtuple('Claim', ['x', 'y', 'w', 'h'])
    re_str = '^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$'

    claims = {}
    for line in data:
        id_, x, y, w, h = map(int, re.search(re_str, line).groups())
        claims[id_] = Claim(x, y, w, h)

    return claims





    

