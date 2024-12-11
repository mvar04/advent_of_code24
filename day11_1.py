with open("day11.txt") as f:
    stones = [int(i) for i in f.read().strip().split()]

for _ in range(25):
    i = 0
    while i < len(stones):
        stone = str(stones[i])
        if stone == '0': 
            stones[i] = 1
            i += 1
        elif len(stone) % 2:
            stones[i] *= 2024
            i += 1
        else:
            stones[i] = int(stone[len(stone)//2:])
            stones.insert(i, int(stone[:len(stone)//2]))
            i += 2
print(len(stones))
