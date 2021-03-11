def sum_two_smallest_numbers(numbers):
    # sort numbers
    sum = 0
    res = sorted(numbers)
    for index, n in enumerate(res):
        if index <= 1:
            sum += n
    return sum
    #return two lowset numbers

print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))
#, 13)
#print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))
#, 19)
#print(sum_two_smallest_numbers([25, 42, 12, 18, 22]))
#, 30)