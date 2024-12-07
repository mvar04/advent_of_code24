with open("day06.txt") as f:
    lines = f.readlines()

width, height = len(lines[0]) - 1, len(lines)
h_walls = [list() for _ in range(height)]
v_walls = [list() for _ in range(width)]

for i, line in enumerate(lines):
    for j, char in enumerate(line.strip()):
        if char == '#': 
            h_walls[i].append(j)
            v_walls[j].append(i)
        elif char == '^':
            pos = (i, j)
            dir = '^'

visited = set()
i, j = pos
while(True):
    if dir == '^': 
        # i_new = (Max of v_walls j < i) + 1 or 0 if none available
        # visited.add(j + width * i) i-- while > i_new
        # if i == 0 end, else dir = '>'
        i_new = -1
        for t in v_walls[j]: 
            if t < i: i_new = max(i_new, t)
        i_new += 1

        while i > i_new:
            visited.add(j + width * i)
            i -= 1
        
        if i_new == 0: break
        else: dir = '>'

    elif dir == '>':
        # j_new = (Min of h_walls i > j) - 1 or width - 1 if none available
        # visited.add(j + width * i) j++ while < j_new
        # if j == width - 1 end, else dir = 'v'
        j_new = width
        for t in h_walls[i]: 
            if t > j: j_new = min(j_new, t)
        j_new -= 1

        while j < j_new:
            visited.add(j + width * i)
            j += 1
        
        if j_new == width - 1: break
        else: dir = 'v'

    elif dir == 'v': 
        # i_new = (Min of v_walls j > i) - 1 or height - 1 if none available
        # visited.add(j + width * i) i++ while < i_new
        # if i == height - 1 end, else dir = '<'
        i_new = height
        for t in v_walls[j]: 
            if t > i: i_new = min(i_new, t)
        i_new -= 1

        while i < i_new:
            visited.add(j + width * i)
            i += 1
        
        if i_new == height - 1: break
        else: dir = '<'

    elif dir == '<':
        # j_new = (Max of h_walls i < j) + 1 or 0 if none available
        # visited.add(j + width * i) j-- while > j_new
        # if j == 0 end, else dir = '^'
        j_new = -1
        for t in h_walls[i]: 
            if t < j: j_new = max(j_new, t)
        j_new += 1

        while j > j_new:
            visited.add(j + width * i)
            j -= 1
        
        if j_new == 0: break
        else: dir = '^'
visited.add(j + width * i)
print(len(visited))