bots = list()
with open("day14.txt") as f:
    for i in f.readlines():
        a, b = i.split()
        ax, ay = a[2:].split(',')
        bx, by = b[2:].split(',')
        bots.append(((ay, ax), (by, bx)))
quad0, quad1, quad2, quad3 = 0, 0, 0, 0
for i in bots:
    y, x = (int(i[0][0]) + int(i[1][0]) * 100) % 103, (int(i[0][1]) + int(i[1][1]) * 100) % 101
    print(x, y)
    if x < 50:
        if y < 51: quad0 += 1
        elif y > 51: quad2 += 1
    elif x > 50:
        if y < 51: quad1 += 1
        elif y > 51: quad3 += 1

print(quad0 * quad1 * quad2 * quad3)