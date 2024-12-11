import copy
with open("day06.txt") as f:
    lines = f.readlines()

width, height = len(lines[0]) - 1, len(lines)
h_walls = [set() for _ in range(height)]
v_walls = [set() for _ in range(width)]

for i, line in enumerate(lines):
    for j, char in enumerate(line.strip()):
        if char == '#':
            h_walls[i].add(j)
            v_walls[j].add(i)
        elif char == '^':
            pos = (i, j)
            dir = '^'

count = 0
for i1 in range(height):
    for j1 in range(width):
        if j1 in h_walls[i1]: continue

        hw = copy.deepcopy(h_walls)
        hw[i1].add(j1)
        vw = copy.deepcopy(v_walls)
        vw[j1].add(i1)

        i, j = pos
        dir = '^'
        for _ in range(10000):
            if dir == '^':
                i_new = -1
                for t in vw[j]:
                    if t < i: i_new = max(i_new, t)
                i_new += 1
                i = i_new
                if i_new == 0: break
                else: dir = '>'

            elif dir == '>':
                j_new = width
                for t in hw[i]:
                    if t > j: j_new = min(j_new, t)
                j_new -= 1
                j = j_new

                if j_new == width - 1: break
                else: dir = 'v'

            elif dir == 'v':
                i_new = height
                for t in vw[j]:
                    if t > i: i_new = min(i_new, t)
                i_new -= 1
                i = i_new

                if i_new == height - 1: break
                else: dir = '<'

            elif dir == '<':
                j_new = -1
                for t in hw[i]:
                    if t < j: j_new = max(j_new, t)
                j_new += 1
                j = j_new

                if j_new == 0: break
                else: dir = '^'
        else:
            count += 1
print(count)           