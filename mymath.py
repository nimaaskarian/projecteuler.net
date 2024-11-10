import math
# this below, is a cool one
import itertools
import numpy as np
def proper_divisors(n):
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            division = n//i
            if i == division or division == n:
                yield i
            else:
                yield i
                yield division

def amicable_numbers(max):
    for i in range(max):
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

def primes(max):
    table = prime_sieve(max)
    for num, is_prime in enumerate(table):
        if is_prime:
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

def tenpow(n):
    return 10**n

def truncate(n, count, is_left=False):
    if is_left:
        return n//tenpow(digit_count(n)-count)

    return n%tenpow(count);

def digit_count(n):
    return int(math.log10(n))+1

def gen_fibo():
    f = 1
    f1 = 1
    f2 = 0
    while True:
        yield f
        f = f1+f2
        f2 = f1
        f1 = f

def gen_digits(num):
    while num:
        yield num%10
        num//=10
