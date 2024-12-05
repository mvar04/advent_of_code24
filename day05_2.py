with open("day05.txt") as f:
    rule_input, seqs = f.read().split("\n\n")

rules = dict()
for i in rule_input.split("\n"):
    x, y = i.split("|")
    x, y = int(x), int(y)
    rules[x] = rules.get(x, set()).union([y,])

seqs = [[int(j) for j in i.split(",")] for i in seqs.strip().split("\n")]

unordered = list()
for seq in seqs:
    for i in range(len(seq) - 1):
        if seq[i + 1] not in rules.get(seq[i], set()): 
            unordered.append(seq)
            break
    
def dogshit_sort(arr):
    changed = True
    while(changed):
        changed = False
        for i in range(len(arr) - 1):
            if arr[i] not in rules.get(arr[i + 1], set()):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                changed = True
    return arr

print(sum([dogshit_sort(i)[len(i) // 2] for i in unordered]))
