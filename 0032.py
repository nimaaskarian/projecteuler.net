from itertools import permutations
from more_itertools import unique_everseen

from utils import s_iter2int

# 1*1 = 7 impossible (9*9   = 81)
# 1*2 = 6 impossible (9*99  = 891)
# 1*3 = 5 impossible (9*999 = 8991)
# a pandigital product its either 
# 1. a 1*4 = 4
# 2. a 2*3 = 4
def pandigital_products():
    base = "123456789"
    for p in permutations(base,9):
        # i should be 4 as its either 1*4 = 4 or 2*3 = 4
        i = 4
        p1 = p[:i]
        # j can be 1 or 2, as in "1"*4 or "2"*3
        for j in range(1, 3):
            p2 =p[i:i+j]
            p3 = p[i+j:]
            n1 = s_iter2int(p1)
            n2 = s_iter2int(p2)
            n3 = s_iter2int(p3)
            if n2 * n3 == n1:
                yield n1

print(sum(unique_everseen(pandigital_products())))
