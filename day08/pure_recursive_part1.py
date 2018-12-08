def process_node(data):
    num_children, num_metadata = data.pop(), data.pop()

    values = [process_node(data) for i in range(num_children)]
    metadata = [data.pop() for i in range(num_metadata)]

    return sum(metadata) + sum(values)

with open('input') as f:
    data = list(map(int, f.read().split()[::-1]))

print(process_node(data))
