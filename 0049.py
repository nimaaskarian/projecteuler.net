import itertools
from mymath import primes
def weird_arthmetic_sequence(primes):
    n = 3330
    for p1 in primes:
        p2 = p1+n
        p3 = p1+n*2
        if p1 in primes and p2 in primes and p3 in primes:
            if sorted(str(p1)) == sorted(str(p2)) and sorted(str(p3)) == sorted(str(p1)):
                yield f"{p1}{p2}{p3}"

primesarr = list(filter(lambda x: x >= 1000,primes(int(1e4))))
_, seq = weird_arthmetic_sequence(primesarr)
print(seq)
