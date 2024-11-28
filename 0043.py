from itertools import permutations
from mymath import primes
import string

from utils import s_iter2int

primearr = primes(18)

def check_primes(s):
    for i in range(7):
        num = s_iter2int(s[i+1:i+4])
        if num % primearr[i] != 0:
            return False
    return True

def substring_divisable_pandigitals():
    for s in permutations(string.digits, 10):
        if s[0] == '0': continue
        if check_primes(s):
            yield s_iter2int(s)

print(sum(substring_divisable_pandigitals()))
