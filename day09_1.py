with open("day09.txt") as f:
    disk = [int(i) for i in f.read().strip()]

ids = [i // 2 if not(i % 2) else -1 for i in range(len(disk))]
print(disk)
print(ids)
print(0, len(ids) - 1)

i, j = 0, len(ids) - 1
while(j > i):
    if ids[j] == -1 or disk[j] == 0: 
        del(ids[j])
        del(disk[j])
        j -= 1
        continue
    if ids[i] != -1:
        i += 1
        continue
        
    if disk[i] > disk[j]:
        disk[i] -= disk[j]
        disk.insert(i, disk[j])
        ids.insert(i, ids[j])
        del(ids[j + 1])    
        del(disk[j + 1])
        i += 1
    else:
        disk[j] -= disk[i]        

        ids[i] = ids[j]
        i += 1

total, i = 0, 0   
for a, b in zip(disk, ids):
    total += ((a + i) * (a + i - 1) - i * (i - 1)) * b / 2
    i += a

print(total)
    