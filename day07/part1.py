import utils
import bisect

free_events, num_depends, blocks = utils.load_data()

ans = ''

while len(free_events) > 0:
    event = free_events.popleft()

    depending_events = blocks[event]
    for depending_event in depending_events:
        num_depends[depending_event] -= 1

        if num_depends[depending_event] == 0:
            bisect.insort_right(free_events, depending_event)

    ans += event

print(ans)
