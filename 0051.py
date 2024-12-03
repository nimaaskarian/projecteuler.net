import itertools
import string
import numpy as np
from mymath import prime_sieve, primes
up = int(1e6)
prime_table = prime_sieve(up)
primes = primes(table=prime_table)
# pp stands for permutation primes...
checked = np.zeros(up, bool)

for i, p in enumerate(primes):
    p_str = str(p)
    max_index = -1
    arr = []
    for size in range(1, len(p_str)):
        for comb in itertools.combinations(range(0, len(p_str)), size):
            count = 1
            arr.append([])
            for ch in string.digits:
                new_p_str = p_str
                for index in comb:
                    if index == 0 and ch == '0':
                        break
                    new_p_str = new_p_str[:index] + ch + new_p_str[index+1:]
                else:
                    new_p = int(new_p_str)
                    if new_p == p:
                        continue
                    if prime_table[new_p]:
                        checked[new_p] = True
                        count += 1
                        arr[-1].append(new_p)
            if max_index == -1 or count >= len(arr[max_index]):
                max_index = len(arr)-1
    if max_index != -1 and len(arr[max_index]) == 8:
        print(min(arr[max_index]))
        break
