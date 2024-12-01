from itertools import count
from mymath import is_prime, proper_divisors


consecutive = 0
for n in count(646):
    prime_div_count = sum(1 for _ in filter(is_prime, proper_divisors(n)))
    if prime_div_count == 4:
        consecutive += 1
        if consecutive == 4: 
            break
    else:
        consecutive = 0

print(n-3)
