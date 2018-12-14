def update(recipes, indices):
    total = recipes[indices[0]] + recipes[indices[1]]
    recipes += [int(i) for i in str(total)]

    for i in range(2):
        indices[i] = (indices[i] + 1 + recipes[indices[i]]) % len(recipes)

recipes = [3, 7]
indices = [0, 1]

M = 430971

while len(recipes) < M + 10:
    update(recipes, indices)

print(''.join(map(str, recipes[M:M+10])))
