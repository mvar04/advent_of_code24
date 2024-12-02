def isValid(diffs):
    left, right = 0, len(diffs) - 1
    
    try:
        trend = diffs[left] / abs(diffs[left])
        while(left != len(diffs)):
            if 0 < diffs[left] * trend <= 3: left += 1
            else: break
    except ZeroDivisionError: pass

    try:
        trend = diffs[right] / abs(diffs[right])
        while(right != -1):
            if 0 < diffs[right] * trend <= 3: right -= 1
            else: break
    except ZeroDivisionError: pass

    if right == -1: return True
    elif right == left:
        if left in [0, len(diffs) - 1]: 
            return True
        elif 3 >= (diffs[left] + diffs[left + 1]) * trend >= 1: 
            return True
    elif left - right == 1:
        if(left == len(diffs) - 1 or right == 0):
            return True
    elif right - left == 1:
        if 3 >= (diffs[left] + diffs[right]) * trend > 0: 
            if diffs[0] * diffs[len(diffs) - 1] > 0:
                return True
    
    return False

input = list()
with open("day02.txt") as f:
    for x in f.readlines():
        diffs = list()
        x = [int(y) for y in x.strip().split()]
        for y in range(len(x) - 1):
            diffs.append(x[y + 1] - x[y])
        input.append(diffs)


print(sum(isValid(diffs) for diffs in input))