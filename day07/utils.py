import re
from collections import defaultdict, deque

def load_data():

    with open('input') as f:
        data = f.read().splitlines()

    re_str = '^Step ([A-Z]) must be finished before step ([A-Z]) can begin.$'

    blocks = defaultdict(set)
    num_depends = defaultdict(int)
    for line in data:
        first, second = re.search(re_str, line).groups()
        blocks[first].add(second)
        num_depends[second] += 1

    free_events = deque(sorted(set(blocks.keys()) - set(num_depends.keys())))
    return free_events, num_depends, blocks
