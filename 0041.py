import itertools
import mymath
from utils import s_iter2int
base = "123456789"

def n_digit_pandigital_primes(n):
    for s in itertools.permutations(base[:n],n):
        if (num := s_iter2int(s)) and mymath.is_prime(num):
            yield num

def biggest_pandigital_prime():
    for n in range(9, -1, -1):
        try:
            return max(n_digit_pandigital_primes(n))
        except ValueError:
            pass
    return 0

print(biggest_pandigital_prime())
