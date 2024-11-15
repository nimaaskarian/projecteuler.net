import itertools
import math

def triangular_numbers():
    for n in itertools.count(1):
        yield (n**2 + n)//2

def divisors(n):
    yield 1
    for i in range(2,math.isqrt(n)+1):
        if n%i == 0:
            yield i
            yield n//i
    yield n

for n in triangular_numbers():
    div_count = sum(1 for _ in divisors(n))
    if div_count > 500:
        print(n)
        break
