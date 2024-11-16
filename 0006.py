def sum_square_diff(num):
    max = num + 1
    sum_squared = sum(range(max))**2
    squared_sum = sum(map(lambda i: i**2,range(max)))
    return sum_squared - squared_sum

print(sum_square_diff(100))
