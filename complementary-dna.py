def DNA_strand(dna):
    result = ''
    for char in dna:
        if(char == 'A'):
            result += "T"
        if(char == 'T'):
            result += "A"
        if(char == 'G'):
            result += "C"
        if(char == 'C'):
            result += "G"
    return result

#print(DNA_strand("AAAA")) #,"TTTT","String AAAA is")
#print(DNA_strand("ATTGC")) #,"TAACG","String ATTGC is")
print(DNA_strand("GTAT")) #,"CATA","String GTAT is")