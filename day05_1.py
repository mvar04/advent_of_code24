with open("day05.txt") as f:
    rule_input, seqs = f.read().split("\n\n")

rules = dict()
for i in rule_input.split("\n"):
    x, y = i.split("|")
    x, y = int(x), int(y)
    rules[x] = rules.get(x, set()).union([y,])

seqs = [[int(j) for j in i.split(",")] for i in seqs.strip().split("\n")]

count = 0
for seq in seqs:
    for i in range(len(seq) - 1):
        if seq[i + 1] not in rules.get(seq[i], set()): break
    else: count += seq[len(seq) // 2]

print(count)