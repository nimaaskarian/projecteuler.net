import sys
from colors import *

def sub_tree(tree, y, x, length):
    return [tree[i][x:x+i+1] for i in range(y, y+length)]

def print_tree(tree, path=None):
    size = len(tree)
    for i in range(size):
        print("  "*(size-i-1), end="")
        for j, item in enumerate(tree[i]):
            if path and j == path[i]:
                print(bcolors.RED+f"{item:02d}"+bcolors.ENDC, end="  ")
            else:
                print(f"{item:02d}", end="  ")
        print()

def find_max_sum_by_sum_tree(tree):
    sum_tree = []
    for i, row in enumerate(tree):
        sum_tree.append([])
        for j in range(len(row)):
            if i == 0:
                sum_tree[i].append(tree[i][j])
            else:
                if j == 0:
                    parents = sum_tree[i-1][j:j+1]
                else:
                    parents = sum_tree[i-1][j-1:j+1]
                current_sum = max(parents)+tree[i][j]
                sum_tree[i].append(current_sum)
    return sum_tree

def read_tree(path: str):
    with open(path) as file:
        return [[int(num_str) for num_str in line.split()] for line in file.read().splitlines()]

if __name__ == "__main__":
    tree = read_tree(sys.argv[1])
    print_tree(tree, [1,0,0,2,3,1,1,1])
    print(max(find_max_sum_by_sum_tree(tree)[-1]))

