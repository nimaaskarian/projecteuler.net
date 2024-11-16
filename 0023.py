import numpy as np
from mymath import proper_divisors

def is_abundant(n):
    return sum(proper_divisors(n)) > n 

def abundants():
    return [is_abundant(n) for n in range(28124)]

def two_abundnat_sums():
    abundants_table = abundants()
    table = np.ones(28124, bool)
    for i, item1 in enumerate(abundants_table):
        for j, item2 in enumerate(abundants_table):
            try:
                if item2 and item1:
                    table[i+j] = False
            except IndexError:
                break

    return table

print(np.sum(np.flatnonzero(two_abundnat_sums())))
    # for i in abundants():
    #     for j in abundants():
    #         if j+i > 28123:
    #             break
    #         yield i+j
# for i in two_abundnat_sums():
#     print(i)
# print(len(list(abundants())))
# list(abundants())
