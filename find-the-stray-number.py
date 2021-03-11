def stray(arr):
    result = 0
    for number in arr:
        if arr.count(number) == 1:
            result = number
    return result


print(stray([1, 1, 1, 1, 1, 1, 2]))
