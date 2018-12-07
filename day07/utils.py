import re
from collections import defaultdict

def load_data():

    with open('input') as f:
        data = f.read().splitlines()

    re_str = '^Step ([A-Z]) must be finished before step ([A-Z]) can begin.$'

    blocks = defaultdict(set)
    depends = defaultdict(set)
    for line in data:
        first, second = re.search(re_str, line).groups()
        blocks[first].add(second)
        depends[second].add(first)

    free_events = set(blocks.keys()) - set(depends.keys())        
    return free_events, depends, blocks
