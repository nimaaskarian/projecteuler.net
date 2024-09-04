num = 1
min = 1
max = 20
for i in range(min, max):
    if num%i != 0:
        for j in range(min, max):
            if (num*j)%i == 0:
                num*=j
                break
print(num)
