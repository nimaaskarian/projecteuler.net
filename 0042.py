import csv, itertools
from string import ascii_uppercase

CHAR_VALUES = {ch: i for i, ch in enumerate(ascii_uppercase, start=1)}

def char_sum(s):
    return sum(CHAR_VALUES[ch] for ch in s)

def triangle_numbers():
    for n in itertools.count(1):
        yield n*(n+1)//2

with open("./0042_words.txt", newline="") as file:
    values = list(char_sum(word) for word in next(csv.reader(file)))

max_value = max(values)
triangles = list(itertools.takewhile(lambda x: x <= max_value, triangle_numbers()))

count = sum(value in triangles for value in values)
print(count)
