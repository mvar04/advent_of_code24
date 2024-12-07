final = list()
terms = list()
with open("day07.txt") as f:
    for line in f.readlines():
        a, b = line.strip().split(":")
        final.append(int(a))
        terms.append([int(c) for c in b.strip().split()])

def valid(terms, final):
    if len(terms) == 1: 
        if terms[0] == final: return final
        else: return 0
    return max(valid([terms[0] + terms[1]] + terms[2:], final), valid([terms[0] * terms[1]] + terms[2:], final), valid([int(str(terms[0]) + str(terms[1]))] + terms[2:], final))

print(sum([valid(terms[i], final[i]) for i in range(len(final))]))