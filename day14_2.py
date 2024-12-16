from copy import deepcopy
pos = list()
vel = list()
with open("day14.txt") as f:
    for i in f.readlines():
        a, b = i.split()
        ax, ay = a[2:].split(',')
        bx, by = b[2:].split(',')
        pos.append([int(ay), int(ax)])
        vel.append((int(by), int(bx)))

i = 0
while True:
    if len(set([i * 101 + j for i, j in pos])) == len(pos): break
    for x in range(len(pos)):
        pos[x][0] = (pos[x][0] + vel[x][0]) % 103
        pos[x][1] = (pos[x][1] + vel[x][1]) % 101
    i += 1
print(i)