def lowest_common_terms(a,b):
    m = min(a,b)
    while m > 1 and a > 1 and b > 1:
        if b%m == 0 and a%m == 0:
            b //= m
            a //= m
        m-=1
    return a,b

def proper_divisors(n):
    import math
    yield 1
    for i in range(2,math.isqrt(n)+1):
        if n%i == 0:
            yield i
            yield n//i

def amicable_numbers():
    import itertools
    for i in itertools.count():
        d = sum(proper_divisors(i))
        if i != d and sum(proper_divisors(d)) == i:
            yield i

def prime_sieve(max):
    import numpy as np
    table = np.ones(max, bool)
    table[0] = False
    table[1] = False
    for i,is_prime in enumerate(table):
        if is_prime:
            for j in range(i*2, max, i):
                table[j] = False
    return table

def is_prime(n):
    import math
    if n == 2: return True
    if n < 2: return False
    if n % 2 == 0: return False
    for i in range(3,math.isqrt(n)+1, 2):
        if n%i == 0:
            return False
    return True

def primes(max=None, table=None):
    import numpy as np
    if table is None:
        table = prime_sieve(max)
    return np.flatnonzero(table)

def nth_prime(n):
    import math
    import numpy as np
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

def digit_count(n, log=None):
    import math
    if log is None:
        log = math.log10
    return int(log(n))+1

def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

def digits(num):
    while num:
        yield num%10
        num//=10

def digits_ltr(num):
    for ch in str(num):
        yield int(ch)

def nth_digit(num, n):
    for _ in range(n-1):
        num//=10
    return  num%10

def nth_digit_left(num, n, base):
    return (num%base**n)//base**(n-1)

def pythagorean_triplets():
    import itertools
    for m in itertools.count(1):
        for n in range(m):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            yield a,b,c

def is_palindrome(n, base):
    import math
    k = digit_count(n, lambda x: math.log(x,2))
    for i in range(k):
        rev = nth_digit_left(n,k-i, base)
        cur = nth_digit_left(n,i+1, base)
        if rev != cur:
            return False
    return True

def palindrome_numbers(base=10):
    import itertools
    for n in itertools.count(1):
        if is_palindrome(n, base):
            yield n
