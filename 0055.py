from mymath import  is_palindrome

def reverse_num(n):
    return int(str(n)[::-1])

def is_lychrel(n):
    for _ in range(50):
        n += reverse_num(n)
        if is_palindrome(n):
            return False
    return True
        
lychrel_count = sum(1 for n in range(1, 10000) if is_lychrel(n))
print(lychrel_count)

