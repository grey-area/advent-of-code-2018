from collections import namedtuple, defaultdict

with open('input') as f:
    data = f.read()[1:-1]

Position = namedtuple('Position', 'x y')
p = Position(0, 0)
distance = 0
p_stack = []
p_dists = defaultdict(lambda: float('inf'))

for char in data:
    if char in 'NWSE':
        if char == 'N':
            p = Position(p.x, p.y + 1)
        if char == 'W':
            p = Position(p.x - 1, p.y)
        if char == 'S':
            p = Position(p.x, p.y - 1)
        if char == 'E':
            p = Position(p.x + 1, p.y)

        distance += 1
        p_dists[p] = min(p_dists[p], distance)
    # Push
    elif char == '(':
        p_stack.append((p, distance))
    # Pop
    elif char == ')':
        p, distance = p_stack.pop()
    # Branch
    elif char == '|':
        p, distance = p_stack[-1]

print(max(p_dists.values()))
