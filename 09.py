import math
def gen_pythagorean_triplets(max):
    a = 2
    b = 2

    for a in range(2, max):
        for b in range(2, max):
            ans = math.sqrt(a**2 + b**2)
            if int(ans) == ans:
                yield (a,b,int(ans))

for a,b,c in gen_pythagorean_triplets(1000):
    if a+b+c == 1000:
        print(a*b*c)
