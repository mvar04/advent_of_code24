with open("day04.txt") as f:
    input = [x.strip() for x in f.readlines()]

for i in range(len(input)):
    input[i] = 'O' + input[i] + 'O'

input.append('O' * len(input[0]))
input.insert(0, 'O' * len(input[0]))

count = 0
for i in range(len(input)):
    for j, val in enumerate(input[i]):
        if val == 'A' and ((input[i - 1][j - 1] == 'M' and input[i + 1][j + 1] == 'S') or (input[i - 1][j - 1] == 'S' and input[i + 1][j + 1] == 'M')) and ((input[i - 1][j + 1] == 'M' and input[i + 1][j - 1] == 'S') or (input[i - 1][j + 1] == 'S' and input[i + 1][j - 1] == 'M')): count += 1
print(count)