from itertools import takewhile
from mymath import is_palindrome, palindrome_numbers

ten_palindromes_e6 = takewhile(lambda x: x < int(1E6), palindrome_numbers())
print(sum(
        filter(lambda n: is_palindrome(n, 2), ten_palindromes_e6)
    ))
