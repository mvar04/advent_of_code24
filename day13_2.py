with open("day13.txt") as f:
    machines = f.read().strip().split("\n\n")

def hcf(x):
    a, b = x
    if a == 0: return b
    if b == 0: return a
    return hcf((b, a % b))

def scale(x, n):
    a, b = x
    return ((a / n, b / n))

def optimal_sol(a, b, c):
    total = 0
    if scale(a, hcf(a)) == scale(b, hcf(b)) != scale(c, hcf(c)):
        #print('1')
        return total
    if c[0] % hcf((a[0], b[0])):
        #print('2')
        return total
    if c[1] % hcf((a[1], b[1])):
        #print('3')
        return total

    if scale(a, hcf(a)) == scale(b, hcf(b)) == scale(c, hcf(c)):
        total += min((c[0] // a[0]) * 3 + c[0] % a[0], (c[0] % b[0]) * 3 + c[0] // b[0])
        #print('4')
        return total

    mod = (a[1] / hcf(a), a[0] / hcf(a))
    b_val = (c[0] * mod[0] - c[1] * mod[1]) / (b[0] * mod[0] - b[1] * mod[1])
    if int(b_val) != b_val:
        #print('5')
        return total
    a_val = (c[0] - b[0] * b_val) / a[0]
    if int(a_val) != a_val:
        #print('6')
        return total
    total += 3 * a_val + b_val
    #print('7')
    return total


total = 0
for i in machines:
    a, b, c = i.strip().split("\n")
    a = (int(a[12:14]), int(a[18:20]))
    b = (int(b[12:14]), int(b[18:20]))
    c = c.split(", ")
    c = (int(c[0][9:]) + 10000000000000, int(c[1][2:]) + 10000000000000)
    total += optimal_sol(a, b, c)
print(total)
