bots = list()
with open("day14.txt") as f:
    for i in f.readlines():
        a, b = i.split()
        ax, ay = a[2:].split(',')
        bx, by = b[2:].split(',')
        bots.append(((int(ay), int(ax)), (int(by), int(bx))))

count = 0
x = 1
board = [[0 for _ in range(101)] for _ in range(103)]
while count < 20:
    for i in bots: board[(i[0][0] + i[1][0] * x) % 103][(i[0][1] + i[1][1] * x) % 101] = 1
    if board[0][50] == 1 and board[1][49] == 1 and board[1][51] == 1 and board[2][48] == 1 and board[2][52] == 1: 
        [print(i[40:60]) for i in board[:5]]
        count += 1 
        print(x) 
    for i in bots: board[(i[0][0] + i[1][0] * x) % 103][(i[0][1] + i[1][1] * x) % 101] = 0
    x += 1
    