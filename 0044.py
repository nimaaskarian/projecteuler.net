import more_itertools

from mymath import is_solvable_to_natural, pentagonals
from utils import benchmark

is_pentagonal = lambda x: is_solvable_to_natural(x, a=3, c_coefficient=2)

def find_d():
    for j,p1 in enumerate(pentagonals(), start=1):
        for p2 in more_itertools.take(10000, pentagonals(j)):
            if is_pentagonal(p2-p1) and is_pentagonal(p2 + p1):
                return p2-p1

print(benchmark(find_d))
