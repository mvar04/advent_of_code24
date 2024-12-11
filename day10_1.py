with open("day10.txt") as f:
    data = [[int(j) for j in i] 
        for i in f.read().strip().split("\n")]

for i in range(len(data)):
    data[i] = [-2] + data[i] + [-2]
data.insert(0, [-2 for _ in range(len(data[0]))])
data.insert(len(data), [-2 for _ in range(len(data[0]))])
start = [(i, j) 
    for i in range(len(data)) 
    for j in range(len(data[0])) 
    if data[i][j] == 0]
w, h = len(data[0]), len(data)
#print(start)
ends = [set() for _ in start]
for i, v in enumerate(start):
    stack = [v]
    while True:
        #if i == 0: print(stack)
        if len(stack) == 0: break
        x, y = stack.pop()
        if data[x][y] == 9:
            ends[i].add(x * h + y)
            continue
        if data[x + 1][y] == data[x][y] + 1:
           stack.append((x + 1, y))
        if data[x][y + 1] == data[x][y] + 1:
            stack.append((x, y + 1))
        if data[x - 1][y] == data[x][y] + 1:
           stack.append((x - 1, y))
        if data[x][y - 1] == data[x][y] + 1:
            stack.append((x, y - 1))
            
print(sum([len(i) for i in ends]))