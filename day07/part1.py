import utils
import bisect

free_events, depends, blocks = utils.load_data()

ans = ''

while len(free_events) > 0:
    event = free_events[0]
    
    depending_events = blocks[event]
    for depending_event in depending_events:
        depends[depending_event].remove(event)
        
        if len(depends[depending_event]) == 0:
            bisect.insort_right(free_events, depending_event)

    free_events.remove(event)
    ans += event

print(ans)
