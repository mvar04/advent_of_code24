A, B = list(), list()
with open('day01.txt') as f:
    for x in f.readlines():
        a, b = x.strip().split('   ')
        A.append(int(a))
        B.append(int(b))

A.sort()
B.sort()

total = sum([abs(a - b) for a, b in zip(A, B)])
print(total)