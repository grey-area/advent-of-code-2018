import utils

graph = utils.load_data()

ans_str = ''
while graph.num_free_events() > 0:
    event = graph.pop_free_event()
    graph.remove_dependencies(event)

    ans_str += event

print(ans_str)
