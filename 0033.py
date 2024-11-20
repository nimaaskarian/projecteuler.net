from itertools import permutations
from mymath import lowest_common_terms
from utils import s_iter2int

base = "123456789"
deno_all = 1
numn_all = 1
for sdeno in permutations(base, 2):
    for snumn in permutations(base, 2):
        if sdeno <= snumn:
            continue
        common = (ch for ch in sdeno if ch in snumn)
        if not any(common):
            continue
        if sdeno == snumn[::-1]:
            continue
        su_deno = s_iter2int(ch for ch in sdeno if ch not in snumn)
        su_numn = s_iter2int(ch for ch in snumn if ch not in sdeno)

        deno = s_iter2int(sdeno)
        numn = s_iter2int(snumn)

        if lowest_common_terms(su_numn,su_deno) == lowest_common_terms(numn, deno):
            deno_all*=su_deno
            numn_all*=su_numn

print(lowest_common_terms(deno_all, numn_all)[0])
