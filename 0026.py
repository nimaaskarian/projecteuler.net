import math
import mymath

def recuring_lengths(min, max):
    for d in range(min, max):
        digits = []
        dividened = 10
        repeat_index = -1
        while True:
            if dividened == 0:
                repeat_index = -1
                break
            while dividened*10 < d:
                digits.append(0)
                dividened*=10
            while dividened < d:
                dividened*=10
            try:
                repeat_index = digits.index((dividened//d, dividened))
            except ValueError:
                pass
            if dividened//d !=0 and repeat_index != -1:
                break
            digits.append((dividened//d, dividened))
            dividened%=d
        yield len(digits[repeat_index:]), d

print(max(recuring_lengths(2,1000))[1])
