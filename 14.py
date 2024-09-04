import numpy as np
def gen_collatz(start):
    while start > 1:
        yield start
        if start % 2 == 0:
            start //= 2
        else:
            start = 3*start+1
    yield 1

def gen_collatz_len(max):
    for i in range(max):
        yield len(list(gen_collatz(i))), i

print(max(gen_collatz_len(1000000),key=lambda e: e[0]))
