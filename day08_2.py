nodes = dict()
with open("day08.txt") as f:
    lines = f.readlines()
    width = len(lines[0]) - 1
    height = len(lines)

    for i, line in enumerate(lines):
        for j, char in enumerate(line.strip()):
            if char == '.': continue
            nodes[char] = nodes.get(char, list()) + [(i, j)]

valid = set()
for v in nodes.values():
    for i in range(len(v) - 1):
        for j in range(i + 1, len(v)):
            diff = (v[j][0] - v[i][0], v[j][1] - v[i][1])
            k = 0
            while 0 <= v[j][0] + k * diff[0] < height and 0 <= v[j][1] + k * diff[1] < width: 
                valid.add(width * (v[j][0] + k * diff[0]) + v[j][1] + k * diff[1])
                #print(width * (v[j][0] + k * diff[0]) + v[j][1] + k * diff[1], v[i], v[j])
                k += 1
            k = 0
            while 0 <= v[i][0] - k * diff[0] < height and 0 <= v[i][1] - k * diff[1] < width: 
                valid.add(width * (v[i][0] - k * diff[0]) + v[i][1] - k * diff[1])
                k += 1

print(len(valid))