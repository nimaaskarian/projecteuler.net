import numpy as np
import math

def triangular_numbers(last):
    last_num, last_triangular = last
    
    current_num = last_num+1
    current_triangular = last_triangular+current_num
    return current_triangular

def count_divisors(num):
    count = np.array(0)
    for i in range(1, (int)(math.sqrt(num)) + 1) : 
        if num%i == 0:
            if num/i == i:
                count+=1
            else:
                count+=2
    return count

def triangular_divisor_length():
    last=(0,0)
    while True:
        last = triangular_numbers(last)
        num = last
        yield (count_divisors(num), num)

for count, num in triangular_divisor_length():
    print(count, num)
    if count >= 500:
        break
