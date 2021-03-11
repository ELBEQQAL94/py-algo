def remove_smallest(numbers):
    result = numbers[:]
    if result:
        result.remove(min(numbers))
    return result


print(remove_smallest([140]))
# , [2, 3, 1, 1])

