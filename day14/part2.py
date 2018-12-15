def update(recipes, indices, target):
    total = recipes[indices[0]] + recipes[indices[1]]

    for i in str(total):
        recipes.append(int(i))
        if len(recipes) >= len(target) and recipes[-len(target):] == target:
            return len(recipes) - len(target)

    for i in range(2):
        indices[i] = (indices[i] + 1 + recipes[indices[i]]) % len(recipes)

recipes = [3, 7]
indices = [0, 1]

target = [4, 3, 0, 9, 7, 1]
ans = None

while ans is None:
    ans = update(recipes, indices, target)

print(ans)
