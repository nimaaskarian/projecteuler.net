import math, itertools
import numpy as np

def lowest_common_terms(a,b):
    m = min(a,b)
    while m > 1 and a > 1 and b > 1:
        if b%m == 0 and a%m == 0:
            b //= m
            a //= m
        m-=1
    return a,b

def proper_divisors(n):
    yield 1
    for i in range(2,math.isqrt(n)+1):
        if n%i == 0:
            yield i
            yield n//i

def amicable_numbers():
    for i in itertools.count():
        d = sum(proper_divisors(i))
        if i != d and sum(proper_divisors(d)) == i:
            yield i

def prime_sieve(max):
    table = np.ones(max, bool)
    table[0] = False
    table[1] = False
    for i,is_prime in enumerate(table):
        if is_prime:
            for j in range(i*2, max, i):
                table[j] = False
    return table

def is_prime(n):
    if n == 2: return True
    if n < 2: return False
    for i in range(3,math.isqrt(n)+1, 2):
        if n%i == 0:
            return False
    return True

def primes(max):
    table = prime_sieve(max)
    for num in np.flatnonzero(table):
        yield num

def nth_prime(n):
    if n <= 0:
        raise ValueError("Argument \"n\" should be a natural (n > 0) number.")
    if n < 6:
        bound = 12
    else:
        bound = math.ceil(n*math.log(n*math.log(n)))
    table = prime_sieve(bound)
    return np.flatnonzero(table)[n-1]

def truncate(n, count, is_left=False):
    if is_left:
        return n//10**(digit_count(n)-count)

    return n%10**count;

def digit_count(n):
    return int(math.log10(n))+1

def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

def digits(num):
    while num:
        yield num%10
        num//=10

def nth_digit(num, n):
    for _ in range(n-1):
        num//=10
    return  num%10

def pythagorean_triplets():
    for m in itertools.count(1):
        for n in range(m):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            yield a,b,c
