import numpy as np
import sys
from colors import bcolors

class Tree():
    def __init__(self, path=None):
        if path is not None:
            with open(path) as file:
                self.tree = [[int(num_str) for num_str in line.split()] for line in file.read().splitlines()]

    def gen_argsort(self):
        for array in self.tree:
            arg_sort = np.argsort(array)

            # yield i,arg_sort
            yield arg_sort

    def gen_biggest_indices(self):
        for y, sorted_indicies in self.gen_argsort():
            yield sorted_indicies[-1]

    def gen_path_sums(self, y=0, x=0, answer=0, path=[]):
        answer = self.tree[y][x] + answer
        path = path+[x]
        if y == len(self.tree) - 1:
            yield answer,path
        else:
            yield from self.gen_path_sums(y+1, x, answer,path)
            yield from self.gen_path_sums(y+1, x+1, answer,path)

    def gen_choices(self, y, x):
        try:
            arr1 = self.tree[y+1]
        except:
            return
        try:
            arr2 = self.tree[y+2]
        except:
            yield arr1[x+1], x+1, None
            yield arr1[x], x, None
            return
        for i in range(2):
            index = x+i+np.argmax(arr2[x+i:x+2+i])
            yield (arr1[x+i] + arr2[index],x+i, index)

    def smart_max_path_sum(self):
        path=[0]
        x = 0
        sum = self.tree[0][0]
        for y in range(0, len(self.tree), 2):
            try:
                value, x1, x2 = max(self.gen_choices(y, x))
            except ValueError:
                break
            path.append(x1)
            if x2 is not None:
                path.append(x2)
            sum += value
            x = x2
        return sum, path

    def divide_max_path_sum(self, length, function=gen_path_sums):
        x = 0
        all_path = []
        all_sum = 0
        for i in range(0,len(self),length):
            sub_tree = self.sub_tree(i,x,length)
            sum, path = max(function(sub_tree))
            all_sum += sum
            path = [index+x for index in path]
            all_path += path
            x = path[-1]
        return all_sum, all_path

    def find_max_sum_by_sum_tree(self):
        sum_tree = []
        for i, row in enumerate(self.tree):
            sum_tree.append([])
            for j in range(len(row)):
                if i == 0:
                    sum_tree[i].append(self.tree[i][j])
                else:
                    if j == 0:
                        parents = sum_tree[i-1][j:j+1]
                    else:
                        parents = sum_tree[i-1][j-1:j+1]
                    current_sum = max(parents)+self.tree[i][j]
                    sum_tree[i].append(current_sum)
        return sum_tree


    def sub_tree(self, y, x, length):
        tree = Tree()
        tree.tree = [self.tree[i][x:x+i+1] for i in range(y, y+length)]
        return tree

    def __len__(self):
        return len(self.tree)

    def print_tree(self, path=None):
        size = len(self.tree)
        for i in range(size):
            print("  "*(size-i-1), end="")
            for j, item in enumerate(self.tree[i]):
                if path and j == path[i]:
                    print(bcolors.RED+f"{item:02d}"+bcolors.ENDC, end="  ")
                else:
                    print(f"{item:02d}", end="  ")
            print()

if __name__ == "__main__":
    tree = Tree(sys.argv[1])
    print(max(tree.find_max_sum_by_sum_tree()[-1]))

