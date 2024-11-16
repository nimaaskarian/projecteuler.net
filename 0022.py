def read_names(path):
    with open(path) as file:
        return [name[1:-1] for name in file.read().split(",")]

def score_names(names):
    names.sort()
    start = ord('A')-1
    for n, name in enumerate(names, start=1):
        base_score = sum(ord(ch)-start for ch in name)
        yield base_score*n

names = read_names("22.txt")
print(sum(score_names(names)))
