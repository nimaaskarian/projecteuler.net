from math import log10
from mymath import gen_fibo


for i,fibo in enumerate(gen_fibo(),start=1):
    if int(log10(fibo))+1 == 1000:
        print(i)
        break
