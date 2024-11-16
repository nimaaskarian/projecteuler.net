from itertools import islice, takewhile
from mymath import amicable_numbers

print(sum(takewhile(lambda x: x < 10000, amicable_numbers())))
