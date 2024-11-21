import math

solutions = dict()
for a in range(1, 1000):
    for b in range(a, 1000):
        if a+b > 1000:
            break
        c, mod = divmod(math.sqrt(a**2+b**2), 1)
        if mod != 0:
            continue
        p = a+b+int(c)
        if p > 1000:
            break
        if solutions.get(p):
            solutions[p] +=1
        else:
            solutions[p] = 1

print(max(solutions.items(), key=lambda kv: kv[1])[0])
