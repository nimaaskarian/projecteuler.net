import itertools
import math

def last_digit(n):
    digit = 0
    while n:
        digit = n % 10
        n //= 10
    return digit

def m_digits_of_n(n,m):
    if m < 0:
        return int(str(n)[m:])
    else:
        return int(str(n)[:m])

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def check_truncatable_primes(n):
    for i in range(1, int(math.log10(n))+2):
        if not is_prime(m_digits_of_n(n, i)):
            return False
        if not is_prime(m_digits_of_n(n, -i)):
            return False
    return True


count = 0
sum = 0
for n in itertools.count(21, 2):
    if count == 11:
        break
    first_digit = n%10
    if first_digit not in [3,7]:
        continue
    if last_digit(n) not in [2,3,5,7]:
        continue
    if check_truncatable_primes(n):
        count+=1
        sum+=n
print(sum)

