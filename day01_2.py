A, B = list(), dict()
with open('day01.txt') as f:
    for x in f.readlines():
        a, b = x.strip().split('   ')
        A.append(int(a))
        B[int(b)] = B.get(int(b), 0) + 1

total = sum([a * B.get(a, 0) for a in A])
print(total)
