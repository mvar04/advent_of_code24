with open("day02.txt") as f:
    input = [[int(y) for y in x.strip().split()] for x in f.readlines()]

safe = 0
for data in input:
    trend = 1 if data[1] - data[0] > 0 else -1
    for i in range(len(data) - 1):
        if 3 >= trend * (data[i + 1] - data[i]) >= 1: pass
        else: 
            print(data)
            break
    else: 
        safe += 1

print(safe)