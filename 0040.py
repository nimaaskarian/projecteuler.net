import itertools
import math
import more_itertools

def champernowne():
    for n in itertools.count(1):
        for digit in str(n):
            yield int(digit)

print(math.prod(
    more_itertools.nth(champernowne(), n)
    for n in map(lambda x: 10**x-1, range(7))
        ))
    
