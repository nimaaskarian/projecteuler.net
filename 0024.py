def gen_permutations(expression,permutation=""):
    if len(expression) == len(permutation):
        yield permutation
    for ch in filter(lambda x: x not in permutation,expression):
        yield from gen_permutations(expression, permutation+ch)

iterator = gen_permutations("0123456789")
milionth_permutation = next(x for i,x in enumerate(iterator) if i==999999)
print(milionth_permutation)
