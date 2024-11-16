from math import log10
from mymath import fibos


for i,fibo in enumerate(fibos(),start=1):
    if int(log10(fibo))+1 == 1000:
        print(i)
        break
