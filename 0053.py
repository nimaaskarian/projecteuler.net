import math
def comb_selection():
    for n in range(1,101):
        for r in range(n):
            comb = math.comb(n, r)
            if comb > int(1e6):
                yield 1

print(sum(comb_selection()))
