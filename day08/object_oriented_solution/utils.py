class Node():
    def __init__(self, num_children, num_metadata):
        self.num_children = num_children
        self.num_metadata = num_metadata

        self.children = []
        self.metadata = []

        self.value = None

    def traverse(self):
        yield self

        for child in self.children:
            yield from child.traverse()

    def compute_value(self):
        if self.value is None:

            if self.num_children == 0:
                self.value = sum(self.metadata)
            else:
                self.value = 0
                for m in self.metadata:
                    if m >= 1 and m <= self.num_children:
                        self.value += self.children[m - 1].compute_value()

        return self.value

def load_data():
    with open('../input') as f:
        data = list(map(int, f.read().split()))

    root_children, root_metadata = data[:2]
    root = Node(root_children, root_metadata)
    stack = [root]
    i = 2

    while len(stack) > 0:
        # We are looking for another child node
        if stack[-1].num_children > len(stack[-1].children):
            num_children, num_metadata = data[i:i + 2]
            node = Node(num_children, num_metadata)
            stack[-1].children.append(node)
            stack.append(node)
            i += 2
        # We are looking for metadata
        elif stack[-1].num_metadata > len(stack[-1].metadata):
            stack[-1].metadata = data[i:i + stack[-1].num_metadata]
            i += stack[-1].num_metadata
        # We've finished getting data for this node
        else:
            stack.pop()

    return root
