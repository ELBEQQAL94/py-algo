def solution(string, ending):
    if not ending:
        return True
    return string[-len(ending):] ==  ending

#print(solution('abcde', 'cde'))
#, True)
#print(solution('abcde', 'abc'))
#, False)
#print(solution('abcde', ''))
#, True)

print(solution('samurai', 'ai'))
# True
