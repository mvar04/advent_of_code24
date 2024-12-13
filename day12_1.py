with open("day12.txt") as f:
    plots = [list(i.strip()) for i in f.read().strip().split()]

width = len(plots[0])
height = len(plots)

for i in range(height):
    plots[i] = ['x'] + plots[i] + ['x']
width += 2

plots.append(['x'] * width)
plots.insert(0, ['x'] * width)
height += 2

perimeter = [[0 for _ in range(width)] for _ in range(height)]
for i in range(1, height - 1):
    for j in range(1, width - 1):
        if plots[i + 1][j] != plots[i][j]: perimeter[i][j] += 1
        if plots[i][j + 1] != plots[i][j]: perimeter[i][j] += 1
        if plots[i - 1][j] != plots[i][j]: perimeter[i][j] += 1
        if plots[i][j - 1] != plots[i][j]: perimeter[i][j] += 1


regions = [[-1 for _ in range(width)] for _ in range(height)]
for i in range(1, height - 1):
    for j in range(1, width - 1):
        if regions[i][j] != -1: continue
        else:
            regions[i][j] = i * width + j
            stack = [(i, j)]
            while(stack):
                a, b = stack.pop()
                if plots[a + 1][b] == plots[a][b] and regions[a + 1][b] != regions[a][b]: 
                    regions[a + 1][b] = regions[a][b]
                    stack.append((a + 1, b))
                if plots[a - 1][b] == plots[a][b] and regions[a - 1][b] != regions[a][b]: 
                    regions[a - 1][b] = regions[a][b]
                    stack.append((a - 1, b))
                if plots[a][b + 1] == plots[a][b] and regions[a][b + 1] != regions[a][b]: 
                    regions[a][b + 1] = regions[a][b]
                    stack.append((a, b + 1))
                if plots[a][b - 1] == plots[a][b] and regions[a][b - 1] != regions[a][b]: 
                    regions[a][b - 1] = regions[a][b]
                    stack.append((a, b - 1))

count = dict()
for i in range(1, height - 1):
    for j in range(1, width - 1):
        a, b = count.get(regions[i][j], [0, 0])
        a += 1
        b += perimeter[i][j]
        count[regions[i][j]] = [a, b]

print(sum([a * b for a, b in count.values()]))
