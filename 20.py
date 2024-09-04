def fact(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return output

def gen_digit(num):
    while num:
        yield num%10
        num//=10

print(sum(gen_digit(fact(100))))
