import itertools

def encode(n):
    return sorted(str(n))
for x in itertools.count(1):
    x2 = x*2
    x3 = x*3
    x4 = x*4
    x5 = x*5
    x6 = x*6
    x_s = encode(x)
    if x_s == encode(x2) and x_s == encode(x3) and x_s == encode(x4) and x_s == encode(x5) and x_s == encode(x6):
        break
print(x)
