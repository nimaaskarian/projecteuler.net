from more_itertools import nth
from mymath import is_solvable_to_natural, pentagonals

is_triangular = lambda x: is_solvable_to_natural(x, a=1, c_coefficient=2)
is_hexagonal = lambda x: is_solvable_to_natural(x, a=2, c_coefficient=1)

penta_tri_hexa = (p for p in pentagonals() if is_triangular(p) and is_hexagonal(p))
print(nth(penta_tri_hexa, 2))
