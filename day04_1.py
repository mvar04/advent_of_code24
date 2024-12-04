with open("day04.txt") as f:
    input = [x.strip() for x in f.readlines()]

for i in range(len(input)):
    input[i] = 'OOO' + input[i] + 'OOO'

for i in range(3):
    input.append('O' * len(input[0]))
    input.insert(0, 'O' * len(input[0]))

count = 0
for i in range(len(input)):
    for j, val in enumerate(input[i]):
        if val == 'X':
            if input[i][j + 1] == 'M' and input[i][j + 2] == 'A' and input[i][j + 3] == 'S': count += 1
            if input[i][j - 1] == 'M' and input[i][j - 2] == 'A' and input[i][j - 3] == 'S': count += 1
            if input[i + 1][j] == 'M' and input[i + 2][j] == 'A' and input[i + 3][j] == 'S': count += 1
            if input[i - 1][j] == 'M' and input[i - 2][j] == 'A' and input[i - 3][j] == 'S': count += 1
            if input[i + 1][j + 1] == 'M' and input[i + 2][j + 2] == 'A' and input[i + 3][j + 3] == 'S': count += 1
            if input[i + 1][j - 1] == 'M' and input[i + 2][j - 2] == 'A' and input[i + 3][j - 3] == 'S': count += 1
            if input[i - 1][j + 1] == 'M' and input[i - 2][j + 2] == 'A' and input[i - 3][j + 3] == 'S': count += 1
            if input[i - 1][j - 1] == 'M' and input[i - 2][j - 2] == 'A' and input[i - 3][j - 3] == 'S': count += 1

print(count)
