from mymath import is_prime, prime_sieve, primes

upbound = int(1e6)
primetable = prime_sieve(upbound)
primearr = primes(table=primetable)

def consecutive_primes():
    for i in range(len(primearr)-1):
        for j in range(i, len(primearr)-1):
            num = sum(primearr[i:j])
            if num >= upbound:
                break
            if primetable[num]:
                yield j-i, num

print(max(consecutive_primes())[1])
