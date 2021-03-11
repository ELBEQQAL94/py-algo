# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python

def row_sum_odd_numbers(n):
    cinema = []
    for j in range(n):
        column = []
        for i in range(n):
            column.append(i+1)
        cinema.append(column)
    return cinema

print(row_sum_odd_numbers(2))