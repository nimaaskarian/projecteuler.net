import itertools

iterator = itertools.permutations("0123456789", 10)
milionth_permutation = next(x for i,x in enumerate(iterator) if i==999999)
print(milionth_permutation)
