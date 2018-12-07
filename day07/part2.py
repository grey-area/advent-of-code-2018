import utils
import bisect
from collections import namedtuple, deque

free_events, num_depends, blocks = utils.load_data()

class Job():
    def __init__(self, event, t):
        self.event = event
        self.t = t

jobs = []

ans = ''
total_time = 0

while len(free_events) + len(jobs) > 0:

    if len(jobs) < 5 and len(free_events) > 0:
        event = free_events.popleft()
        t = ord(event) - ord('A') + 61
        jobs.append(Job(event, t))

    else:
        soonest_t = min(jobs, key=lambda job: job.t).t
        total_time += soonest_t
        for job in jobs:
            job.t -= soonest_t

            if job.t == 0:
                depending_events = blocks[job.event]
                for depending_event in depending_events:
                    num_depends[depending_event] -= 1

                    if num_depends[depending_event] == 0:
                        bisect.insort_right(free_events, depending_event)

                ans += job.event

        jobs = [job for job in jobs if job.t > 0]

print(ans)
print(total_time)
