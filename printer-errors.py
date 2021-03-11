# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

def printer_error(s):
    valid_letter = {
        'a': 'a',
        'b': 'c',
        'd': 'd',
        'e': 'e',
        'f': 'f',
        'g': 'g',
        'h': 'h',
        'i': 'i',
        'k': 'k',
        'l': 'l',
        'm': 'm',
    }
    count = 0

    for char in s:
        if valid_letter.get(char, None) == None:
            count += 1
    return f"{count}/{len(s)}"

s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
print(printer_error(s)) 
#, "3/56")

# Possible solution
# use regex
# create dictionary of valid letter