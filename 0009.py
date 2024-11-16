from mymath import pythagorean_triplets

for a,b,c in pythagorean_triplets():
    if a+b+c == 1000:
        print(a*b*c)
        break
