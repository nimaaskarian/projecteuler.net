from itertools import product
from math import prod
from fractions import Fraction

def digit_cancelling_fractions():
    for d in range(2, 10):
        for n, m in product(range(1, d), range(d+1, 10)):
            if Fraction(n,d) == Fraction(n*10+m,d+10*m):
                yield Fraction(n, d)

print(prod(digit_cancelling_fractions()).denominator)
