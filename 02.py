def yield_fibo(max):
    f_2 = 1
    f_1 = 2
    f = 0
    yield f_2
    yield f_1
    while f_1 + f_2 < max:
        f = f_1 + f_2
        yield f
        f_2 = f_1
        f_1 = f

sum = sum(filter(lambda i: i%2==0,yield_fibo(4000000)))
print(sum)
