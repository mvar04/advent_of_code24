with open("day03.txt") as f:
    input = f.read()
input += 'X'

filtered = str()

i = 0
while True:
    copy = i
    while input[i: i + 7] != "don't()": 
        i += 1
        if i >= len(input) - 6: break
    filtered += input[copy : i]

    copy = i
    while input[i: i + 4] != "do()": 
        i += 1
        if i >= len(input) - 3: break
    if i >= len(input)- 3: break


total = 0
for i in range(len(filtered) - 3):
    if filtered[i: i+4] == 'mul(':
        j = i + 4
        while filtered[j] != ')':
            if '0' <= filtered[j] <= '9' or filtered[j] == ',': j += 1
            else: break
        else: 
            a = filtered[i + 4: j].split(',')
            if(len(a) == 2): total += int(a[0]) * int(a[1])

print(total)

