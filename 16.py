def gen_digits(num):
    while num:
        yield num%10
        num //= 10

print(sum(gen_digits(2**1000)))
