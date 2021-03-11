# def xo(s):
#     coun_x = 0
#     coun_o = 0
#     for char in s:
#         if(char.lower() == 'x'):
#             coun_x += 1
#         if(char.lower() == 'o'):
#             coun_o += 1
#     return coun_x == coun_o

def xo(s):
    return s.lower().count('x') == s.lower().count('o')

#print(xo('xo')) #, 'True expected')
#print(xo('xo0')) #, 'True expected')
print(xo('xxxoo')) #, 'False expected')