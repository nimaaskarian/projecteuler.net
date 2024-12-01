import math
def prime_factors(num):
    factors = []
    for i in range(2, math.isqrt(num)):
        if num%i == 0:
            if not any(filter(lambda fac: i%fac==0,factors)):
                factors.append(i)

    return factors
num = 600851475143
print(max(prime_factors(num)))
