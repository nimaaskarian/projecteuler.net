import itertools
from math import factorial
from mymath import digits

facts = tuple(factorial(d) for d in range(10))
digit_factorials = 0
for n in range(10, facts[9]*9):
    digit_factorial_sum = sum(facts[d] for d in digits(n))
    if digit_factorial_sum == n:
        digit_factorials+=n
print(digit_factorials)
