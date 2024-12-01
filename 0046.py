import itertools
from math import sqrt
from mymath import is_prime

primes = [2]
def check_n_has_conjucture(n):
    for p in primes:
        if sqrt((n - p)//2) % 1 == 0:
            return True
    return False

for n in itertools.count(3, step=2):
    if is_prime(n):
        primes.append(n)
    else:
        if not check_n_has_conjucture(n):
            print(n)
            break
