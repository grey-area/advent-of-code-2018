import utils

root = utils.load_data()
ans = 0

for node in root.traverse():
    ans += sum(node.metadata)

print(ans)
