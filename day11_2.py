with open("day11.txt") as f:
    stones = [int(i) for i in f.read().strip().split()]

precalc = [[-1 for _ in range(10000)] for _ in range(76)]
precalc[0] = [1 for _ in range(10000)]

def num_stones(stone, steps):
    if stone < 10000 and precalc[steps][stone] != -1: return precalc[steps][stone]
    if steps == 0: return 1
    if stone == 0: return precalc[steps - 1][1]
    length = len(str(stone))
    if length % 2: return num_stones(stone * 2024, steps - 1)
    return num_stones(int(str(stone)[:length//2]), steps - 1) + num_stones(int(str(stone)[length//2:]), steps - 1)

for i in range(1, 76):
    for j in range(10000):
        precalc[i][j] = num_stones(j, i)

print(sum([num_stones(i, 75) for i in stones]))