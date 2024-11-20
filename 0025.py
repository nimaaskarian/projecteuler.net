from mymath import digit_count, fibonacci

for i,fibo in enumerate(fibonacci(),start=1):
    if digit_count(fibo) == 1000:
        print(i)
        break
