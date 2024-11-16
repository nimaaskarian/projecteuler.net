def is_palindrome(num):
    num_str = str(num)
    mid = (len(num_str)+1)//2

    return num_str[:mid] == num_str[:mid-1:-1]

def gen_palindrome(min, max):
    for i in range(min, max):
        for j in range(min, max):
            if is_palindrome(i * j):
                yield i*j

print(max(gen_palindrome(99,1000)))
