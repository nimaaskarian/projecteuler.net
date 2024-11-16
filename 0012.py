import itertools
import mymath

def triangular_numbers():
    for n in itertools.count(1):
        yield (n**2 + n)//2

for n in triangular_numbers():
    div_count = sum(1 for _ in mymath.proper_divisors(n))
    if div_count > 500:
        print(n)
        break
