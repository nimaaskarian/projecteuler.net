from itertools import permutations
from more_itertools import nth

milionth_permutation = nth(permutations("0123456789", 10), 999999)
print("".join(milionth_permutation))
