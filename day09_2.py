
with open("day09.txt") as f:
    disk = [int(i) for i in f.read().strip()]

ids = [i // 2 if not(i % 2) else -1 for i in range(len(disk))]

j = len(ids) - 1
while(j >= 0):
    if ids[j] == -1 or disk[j] == 0: 
        j -= 1
        continue
    i = 0
    while (i < j):
        if ids[i] != -1: 
            i += 1
            continue
        if disk[i] > disk[j]:
            disk[i] -= disk[j]
            disk.insert(i, disk[j])
            ids.insert(i, ids[j])
            j += 1
            ids[j] = -1   
            break
        if disk[i] == disk[j]:
            ids[i] = ids[j]
            ids[j] = -1
            break
        i += 1
    j -= 1

ids = [i if i >= 0 else 0 for i in ids]
total, i = 0, 0   
for a, b in zip(disk, ids):
    total += ((a + i) * (a + i - 1) - i * (i - 1)) * b / 2
    i += a

print(total)