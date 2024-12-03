with open("day03.txt") as f:
    input = f.read()
input += 'X'

total = 0
for i in range(len(input) - 3):
    if input[i: i+4] == 'mul(':
        j = i + 4
        while input[j] != ')':
            if '0' <= input[j] <= '9' or input[j] == ',': j += 1
            else: break
        else: 
            a = input[i + 4: j].split(',')
            if(len(a) == 2): total += int(a[0]) * int(a[1])

print(total)