from itertools import filterfalse, takewhile
from mymath import fibonacci

even_fibos = filterfalse(lambda x: x%2,fibonacci())
even_fibos_below_4m = takewhile(lambda x: x < 4000000, even_fibos)
sum = sum(even_fibos_below_4m)
print(sum)
