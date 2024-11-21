import math

solutions = dict()
for a in range(1, 1000):
    for b in range(a, 1000-a):
        if (c := math.sqrt(a**2+b**2)) != int(c):
            continue
        p = a+b+int(c)
        if p > 1000:
            break
        solutions[p] = solutions.get(p, 0) + 1

print(max(solutions, key=solutions.get))
