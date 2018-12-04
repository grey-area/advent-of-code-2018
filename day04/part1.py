import re
from datetime import datetime
import numpy as np
from collections import defaultdict

with open('input') as f:
    data = sorted(f.read().splitlines())

re_str = '^\[(.+)\] (.+)$'

guard_sleep_counts = defaultdict(lambda: np.zeros(60, dtype=np.int32))

id_ = -1
start = 0

for line in data:
    date_str, event_str = re.search(re_str, line).groups()

    if event_str.startswith('Guard'):
        id_ = int(re.search('\d+', event_str).group())
    elif event_str.startswith('falls'):
        start = int(date_str[-2:])
    elif event_str.startswith('wakes'):
        end = int(date_str[-2:])
        guard_sleep_counts[id_][start:end] += 1

guard_id, sleep_counts = max(guard_sleep_counts.items(), key=lambda x: np.sum(x[1]))
print(guard_id * np.argmax(sleep_counts))
