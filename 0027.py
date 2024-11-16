import itertools
import mymath

def quadratic_prime_counts_and_multiples(abs_max):
    for a in range(-(abs_max-1), abs_max):
        for b in range(-(abs_max-1), abs_max):
            for n in itertools.count():
                if not mymath.is_prime(n*n + a*n + b):
                    break
            yield n, a, b

_, a, b = max(quadratic_prime_counts_and_multiples(1000))
print(a*b)
