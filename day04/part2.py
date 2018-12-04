import utils
import numpy as np
from collections import namedtuple

guard_sleep_counts = utils.load_data()

# For storing guard id, the minute he sleeps the most, and the
# count for that minute
Guard_max = namedtuple('Guard_max',
                       ['id_',
                        'max_minute',
                        'max_times'])

# A list of the most slept minute and number of times for each guard
guard_max_list = [Guard_max(k, *max(enumerate(v), key=lambda x: x[1])) for k, v in guard_sleep_counts.items()]

# The guard who sleeps the most in a given minute
target_guard = max(guard_max_list, key=lambda x: x.max_times)

print(target_guard.id_ * target_guard.max_minute)
