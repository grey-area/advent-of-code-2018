import utils
import bisect
from collections import namedtuple, deque

graph = utils.load_data()

class Job():
    def __init__(self, event, t):
        self.event = event
        self.t = t

jobs = []

ans_str = ''
total_time = 0

while graph.num_free_events() + len(jobs) > 0:

    if len(jobs) < 5 and graph.num_free_events() > 0:
        event = graph.pop_free_event()
        t = ord(event) - ord('A') + 61
        jobs.append(Job(event, t))

    else:
        soonest_t = min(jobs, key=lambda job: job.t).t
        total_time += soonest_t
        for job in jobs:
            job.t -= soonest_t

            if job.t == 0:
                graph.remove_dependencies(job.event)
                ans_str += job.event

        jobs = [job for job in jobs if job.t > 0]

print(ans_str)
print(total_time)
