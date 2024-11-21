from collections import deque
from mymath import digits_ltr, prime_sieve, primes
from utils import iter2int

table = prime_sieve(int(1E6))
def all_rotations_prime(p):
    digs = deque(digits_ltr(p))
    for _ in range(len(digs)):
        digs.rotate(1)
        r = iter2int(digs)
        if not table[r]:
            return False
    return True

count = sum(1
            for p in primes(table=table)
            if all_rotations_prime(p)
        )
print(count)
