import itertools

def encode(n):
    return sorted(str(n))

def six_multiples_has_same_digits(x):
    x_s = encode(x)
    for k in range(2,7):
        if x_s != encode(x*k):
            return False
    return True

for x in itertools.count(1):
    if six_multiples_has_same_digits(x):
        break
print(x)
