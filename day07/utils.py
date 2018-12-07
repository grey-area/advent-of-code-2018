import re
import bisect
from collections import defaultdict, deque


class DependencyGraph():
    def __init__(self, blocks, num_depends, free_events):
        self.blocks = blocks
        self.num_depends = num_depends
        self.free_events = free_events

    def pop_free_event(self):
        return self.free_events.popleft()

    def remove_dependencies(self, event):
        depending_events = self.blocks[event]
        for depending_event in depending_events:
            self.num_depends[depending_event] -= 1

            if self.num_depends[depending_event] == 0:
                bisect.insort_right(self.free_events, depending_event)

    def num_free_events(self):
        return len(self.free_events)


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

    return DependencyGraph(blocks, num_depends, free_events)
