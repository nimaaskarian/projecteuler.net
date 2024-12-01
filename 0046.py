import itertools
from mymath import is_prime

primes = []
def check_n_has_conjucture(n):
    for p in primes:
        for sq in map(lambda x: x*x, itertools.count(1)):
            if 2*sq + p == n:
                return True
            if 2*sq + p > n:
                break
    return False

for n in itertools.count(2):
    if is_prime(n):
        primes.append(n)
    elif n % 2 == 1:
        if not check_n_has_conjucture(n):
            print(n)
            break
