import itertools
from mymath import digits

fifth_powers = tuple(d**5 for d in range(10))
digit_factorials = 0
for upperbound in itertools.count(1):
    if fifth_powers[9]*upperbound <= 10**upperbound:
        break

for n in range(10, fifth_powers[9]*(upperbound-1)):
    digit_factorial_sum = sum(fifth_powers[d] for d in digits(n))
    if digit_factorial_sum == n:
        digit_factorials+=n
print(digit_factorials)
