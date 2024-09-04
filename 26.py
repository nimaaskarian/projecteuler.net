# print(10**8//7)
from mymath import gen_digits


for i in range(2,1000):
    num = 10**1000//i
    digits = list(gen_digits(num))

