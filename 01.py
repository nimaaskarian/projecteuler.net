multiples = filter(lambda i: i%5 == 0 or i%3 == 0,range(1000))
multiples_sum = sum(multiples)

print(multiples_sum)
