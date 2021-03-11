import string

# def to_jaden_case(s):
#     return string.capwords(s)

def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))