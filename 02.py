def fibos(max):
    fn = f1 = f2 = 1
    while fn < max:
        yield fn
        fn = f1 + f2
        f2 = f1
        f1 = fn

sum = sum(filter(lambda i: i%2==0,fibos(4000000)))
print(sum)
